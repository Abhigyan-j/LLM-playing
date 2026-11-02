# LLM Playground

An interactive web application for experimenting with large language models (LLMs). This playground allows you to interact with GPT-2 and Qwen models, adjust decoding strategies, and explore how different parameters affect text generation.

## 🚀 Live Demo

**Try it now:** [https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/](https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/)

## Features

- **Multiple Models**: Experiment with GPT-2 (completion model) and Qwen (instruction-tuned model)
- **Decoding Strategies**: Choose from greedy, top-k, or top-p (nucleus) sampling
- **Adjustable Parameters**: Fine-tune temperature, max tokens, top-k, and top-p values
- **Interactive UI**: Clean, user-friendly interface built with Streamlit
- **Real-time Generation**: Generate text instantly with your custom prompts

## Local Setup

### Prerequisites

- Python 3.8-3.11 (Python 3.11 recommended)
- pip or conda package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/nicolairobles/llm-playground.git
cd llm-playground
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

## Deployment to Streamlit Community Cloud

This application is designed to be deployed on Streamlit Community Cloud for free.

### Steps:

1. **Push your code to GitHub** (if not already done):
   - Ensure all files are committed and pushed to your repository

2. **Deploy on Streamlit Community Cloud**:
   - Navigate to [https://share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository: `llm-playground`
   - Branch: `main`
   - Main file: `app.py`
   - Click "Deploy"

3. **Access your app**:
   - Your app will be available at your unique Streamlit subdomain
   - **Live Demo:** [https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/](https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/)
   - The app will automatically update whenever you push changes to the main branch

### Notes for Deployment

- **Model Download**: On first run, the app will download models from Hugging Face (GPT-2 ~500MB, Qwen ~1GB). This happens automatically but may take a few minutes.
- **Memory Requirements**: Ensure your Streamlit Community Cloud instance has sufficient memory. The free tier should handle these models, but generation may be slower.
- **Caching**: Models are cached using `@st.cache_resource` to avoid reloading on every interaction.

## Usage Guide

### Model Selection

- **GPT-2**: A completion model that continues text in the same style. Best for creative writing, story continuation, or text completion tasks.
- **Qwen**: An instruction-tuned model that interprets prompts as requests. Best for questions, instructions, and conversational tasks.

### Decoding Strategies

- **Greedy**: Always selects the most probable next token. Most deterministic but can be repetitive.
- **Top-k**: Samples from the top k most likely tokens. Good balance between creativity and coherence.
- **Top-p (Nucleus)**: Samples from tokens whose cumulative probability exceeds p. Often produces more diverse outputs.

### Parameters

- **Temperature**: Controls randomness (0.1-2.0). Lower values = more focused, higher values = more creative.
- **Max Tokens**: Maximum number of tokens to generate (10-200).
- **Top-k**: Number of top tokens to consider (only for top-k strategy).
- **Top-p**: Cumulative probability threshold (only for top-p strategy).

## Model Information

- **GPT-2**: 124M parameter model from OpenAI. Uses GPT-2 tokenizer.
- **Qwen/Qwen2.5-0.5B-Instruct**: 500M parameter instruction-tuned model from Qwen. Uses Qwen tokenizer with special instruction formatting.

## Performance Notes

- First model load may take 1-2 minutes as models are downloaded from Hugging Face
- Subsequent loads are faster due to caching
- Text generation speed depends on model size and hardware
- On Streamlit Community Cloud free tier, generation may take 5-15 seconds per request

## Troubleshooting

### Model Download Issues
- Ensure you have a stable internet connection
- Check that Hugging Face is accessible from your location
- Models are cached locally after first download

### Memory Errors
- Reduce max_tokens if you encounter memory issues
- Try using GPT-2 instead of Qwen if memory is limited
- On Streamlit Cloud, the free tier should handle these models

### Generation Errors
- Check that your prompt is not too long (keep under 1000 characters)
- Ensure all parameters are within valid ranges
- Try a simpler prompt if generation fails

## License

This project is open source and available for educational and portfolio purposes.

## Acknowledgments

- Built using [Streamlit](https://streamlit.io/)
- Models provided by [Hugging Face](https://huggingface.co/)
- Based on educational content from AI Engineering Course

