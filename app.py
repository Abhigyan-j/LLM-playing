import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import gc

# Page configuration
st.set_page_config(
    page_title="LLM Playground",
    page_icon="🚀",
    layout="wide"
)

# Title and description
st.title("LLM Playground")
st.markdown("""
Interactive playground to experiment with GPT-2 and Qwen models. 
Adjust decoding strategies, temperature, and other parameters to see how they affect text generation.
""")

# Force CPU usage to avoid GPU memory issues on Streamlit Cloud
device = "cpu"
torch_dtype = torch.float32

# Model loading with caching - optimized for memory
@st.cache_resource
def load_gpt2():
    """Load GPT-2 model and tokenizer with memory optimizations"""
    model = AutoModelForCausalLM.from_pretrained(
        "gpt2",
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True
    )
    model.to(device)
    model.eval()  # Set to evaluation mode to save memory
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    return model, tokenizer

@st.cache_resource
def load_qwen():
    """Load Qwen model and tokenizer with memory optimizations"""
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-0.5B-Instruct",
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True
    )
    model.to(device)
    model.eval()  # Set to evaluation mode to save memory
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    return model, tokenizer

# Generation function with memory optimizations
def generate(model, tokenizer, prompt, strategy="greedy", max_new_tokens=128, temperature=1.0, top_k=50, top_p=0.9):
    """
    Generate text using the specified model and decoding strategy.
    Optimized for memory efficiency.
    
    Args:
        model: The loaded model
        tokenizer: The corresponding tokenizer
        prompt: Input text prompt
        strategy: One of "greedy", "top_k", or "top_p"
        max_new_tokens: Maximum number of tokens to generate
        temperature: Sampling temperature
        top_k: Top-k sampling parameter
        top_p: Top-p (nucleus) sampling parameter
    
    Returns:
        Generated text string
    """
    try:
        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
        
        # Memory-efficient generation settings
        generation_config = {
            "max_new_tokens": max_new_tokens,
            "pad_token_id": tokenizer.eos_token_id,
            "do_sample": strategy != "greedy",
        }
        
        if strategy == "greedy":
            generation_config["do_sample"] = False
        elif strategy == "top_k":
            generation_config["temperature"] = temperature
            generation_config["top_k"] = top_k
        elif strategy == "top_p":
            generation_config["temperature"] = temperature
            generation_config["top_p"] = top_p
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
        
        with torch.no_grad():  # Disable gradient computation to save memory
            outputs = model.generate(inputs, **generation_config)
        
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Clean up
        del inputs, outputs
        gc.collect()
        
        return result
    except Exception as e:
        return f"Error generating text: {str(e)}"

# Sidebar for settings
st.sidebar.header("⚙️ Settings")

# Model selection
model_choice = st.sidebar.selectbox(
    "Select Model:",
    ["GPT-2", "Qwen"],
    help="GPT-2 is a completion model. Qwen is an instruction-tuned model."
)

# Strategy selection
strategy = st.sidebar.selectbox(
    "Decoding Strategy:",
    ["greedy", "top_k", "top_p"],
    help="Greedy: always picks most likely token. Top-k: samples from top k tokens. Top-p: nucleus sampling."
)

# Temperature slider
temperature = st.sidebar.slider(
    "Temperature:",
    min_value=0.1,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Higher values make output more random. Lower values make it more deterministic."
)

# Max tokens slider (reduced default for memory efficiency)
max_tokens = st.sidebar.slider(
    "Max Tokens:",
    min_value=10,
    max_value=150,  # Reduced max to save memory
    value=30,  # Reduced default from 50 to 30
    step=10,
    help="Maximum number of tokens to generate. Lower values use less memory."
)

# Top-k parameter (only shown when strategy is top_k)
top_k_value = 50
if strategy == "top_k":
    top_k_value = st.sidebar.slider(
        "Top-k:",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        help="Number of top tokens to consider for sampling."
    )

# Top-p parameter (only shown when strategy is top_p)
top_p_value = 0.9
if strategy == "top_p":
    top_p_value = st.sidebar.slider(
        "Top-p:",
        min_value=0.1,
        max_value=1.0,
        value=0.9,
        step=0.05,
        help="Nucleus sampling: cumulative probability threshold."
    )

# Main content area
st.header("Prompt Input")

# Prompt input
prompt = st.text_area(
    "Enter your prompt:",
    value="Once upon a time",
    height=100,
    help="Type your prompt here. For Qwen, you can use instruction-style prompts."
)

# Generate button
if st.button("Generate", type="primary", use_container_width=True):
    if not prompt.strip():
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Loading model and generating text..."):
            try:
                # Load appropriate model (only one at a time)
                if model_choice == "GPT-2":
                    model, tokenizer = load_gpt2()
                    formatted_prompt = prompt
                else:  # Qwen
                    model, tokenizer = load_qwen()
                    # Format prompt for instruction-tuned model
                    formatted_prompt = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
                
                # Generate text
                result = generate(
                    model, 
                    tokenizer, 
                    formatted_prompt,
                    strategy=strategy,
                    max_new_tokens=max_tokens,
                    temperature=temperature,
                    top_k=top_k_value,
                    top_p=top_p_value
                )
                
                # Display result
                st.header("Generated Output")
                st.markdown(f"**Model:** {model_choice} | **Strategy:** {strategy} | **Temperature:** {temperature}")
                st.markdown("---")
                st.write(result)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("If you're experiencing memory issues, try: 1) Using GPT-2 instead of Qwen, 2) Reducing max tokens, 3) Using greedy strategy.")

# Footer
st.markdown("---")
st.markdown("""
### 💡 Tips
- **GPT-2**: Best for text completion. Give it a sentence or paragraph to continue.
- **Qwen**: Best for instructions and questions. Try asking it questions or giving it tasks.
- **Greedy**: Most deterministic, but can be repetitive.
- **Top-k/Top-p**: More creative and diverse outputs.
- **Temperature**: Lower (0.1-0.5) for focused outputs, higher (1.0-2.0) for creative outputs.

---
**🔗 [View on GitHub](https://github.com/nicolairobles/llm-playground)**
""")

