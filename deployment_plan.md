# Deploy Interactive LLM Playground as Portfolio Web App

This ExecPlan is a living document. The sections `Progress`, `Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective` must be kept up to date as work proceeds.

This document must be maintained in accordance with PLANS.md located at `/Users/tempUser/Projects/ai-engineering-course/PLANS.md`.

## Purpose / Big Picture

After completing this plan, you will have a live, interactive LLM playground web application hosted for free on Streamlit Community Cloud. Visitors can experiment with GPT-2 and Qwen models, adjust decoding strategies (greedy, top-k, top-p), modify temperature settings, and generate text in real-time through a polished web interface. The app will be accessible via a public URL that you can share in your portfolio, and it will automatically update whenever you push changes to your GitHub repository.

To see it working, you will navigate to your deployed Streamlit app URL: [https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/](https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/) and observe a clean interface with input fields for prompts, dropdowns for model and strategy selection, sliders for temperature and max tokens, and a generate button that produces model outputs in real-time.

**This plan uses an automated multi-agent workflow that minimizes human involvement.** Once triggered, three specialized agents work in sequence using Git work trees to develop, review, and validate the code until the project is complete. The workflow operates on a separate GitHub repository that you will create, ensuring clean separation from the original project.

## Progress

- [x] User creates separate GitHub repository for the deployment project
- [x] User initializes repository with this ExecPlan and source notebook reference
- [x] Agent 1 (Development): Set up git work tree and create feature branch
- [x] Agent 1 (Development): Convert notebook section 5 into Streamlit application
- [x] Agent 1 (Development): Extract and refactor model loading and generation functions
- [x] Agent 1 (Development): Create polished Streamlit UI with proper layout and styling
- [x] Agent 1 (Development): Add requirements.txt with all necessary dependencies
- [x] Agent 1 (Development): Create README.md with setup and deployment instructions
- [x] Agent 1 (Development): Create pull request with implementation
- [x] Agent 2 (Code Review): Review PR for code quality, best practices, and correctness
- [x] Agent 3 (Plan Alignment): Review PR against ExecPlan for completeness and alignment
- [x] Agent 3 (Plan Alignment): Resolve any merge conflicts if they arise
- [x] Agent 3 (Plan Alignment): Merge PR if all checks pass, or request fixes from Agent 1
- [x] Agent 1 (Development): Address review feedback and update PR if needed
- [ ] Final verification: Test deployment readiness and document live URL

## Surprises & Discoveries

(To be populated during implementation)

## Decision Log

- Decision: Use Streamlit instead of Gradio or other alternatives
  Rationale: User has prior experience with Streamlit, it offers free hosting via Community Cloud, requires minimal setup, and produces professional-looking UIs without frontend coding. Research confirms it's the lowest-cost option (free) and simplest deployment path for portfolio projects.
  Date/Author: 2025-01-27

- Decision: Deploy to Streamlit Community Cloud rather than self-hosting
  Rationale: Completely free for public apps, one-click deployment via GitHub integration, automatic updates on git push, no server management required, and provides a clean `.streamlit.app` subdomain perfect for portfolio sharing.
  Date/Author: 2025-01-27

- Decision: Convert only section 5 (interactive playground) rather than the entire notebook
  Rationale: The user specifically requested section 5 and everything below it. Section 5 is the interactive playground that makes sense as a standalone web app. The earlier sections (tokenization, model inspection) are educational but less suitable for an interactive portfolio piece.
  Date/Author: 2025-01-27

- Decision: Use separate GitHub repository for deployment project
  Rationale: Clean separation from original course project, allows independent version control, easier to share as portfolio piece, and enables automated workflow without affecting main project.
  Date/Author: 2025-01-27

- Decision: Implement multi-agent workflow with git work trees
  Rationale: Minimizes human involvement by automating development, code review, and plan alignment. Git work trees allow parallel work without conflicts. Three specialized agents ensure quality: one for development, one for code review, one for plan alignment and conflict resolution.
  Date/Author: 2025-01-27

- Decision: Use pull request workflow for agent collaboration
  Rationale: Standard Git workflow enables code review, maintains history, allows iterative improvements, and provides clear checkpoints. Agents can work asynchronously with clear handoff points.
  Date/Author: 2025-01-27

## Outcomes & Retrospective

(To be populated upon completion)

## Context and Orientation

The current project contains a Jupyter notebook (`lm_playground.ipynb`) located at `/Users/tempUser/Projects/ai-engineering-course/project_1/lm_playground.ipynb`. This notebook is an educational project that teaches LLM fundamentals through hands-on exercises. Section 5 (starting around cell 52) contains an optional interactive playground built with `ipywidgets` that allows users to experiment with text generation using GPT-2 and Qwen models.

The notebook uses the following key libraries:
- `torch` (PyTorch) for model operations
- `transformers` (Hugging Face) for loading and using pre-trained models
- `tiktoken` for tokenization utilities
- `ipywidgets` for the current interactive UI (which we'll replace with Streamlit)

The project has a conda environment defined in `env.yaml` with Python 3.11 and the dependencies listed above. For deployment, we need to convert this to a `requirements.txt` format that Streamlit Community Cloud can use.

Streamlit is a Python framework that turns Python scripts into web applications. Instead of writing HTML, CSS, or JavaScript, you write Python code that Streamlit renders as a web UI. Streamlit Community Cloud is a free hosting service that automatically builds and deploys Streamlit apps from GitHub repositories. When you connect your GitHub repo, it detects your Streamlit app file (typically `app.py`), installs dependencies from `requirements.txt`, and hosts it at a public URL.

**Multi-Agent Workflow Architecture:** This plan uses three specialized agents that work autonomously using Git work trees. A Git work tree is a separate working directory that shares the same Git repository but allows independent checkouts. This enables agents to work in parallel without interfering with each other. The workflow operates on a separate GitHub repository that you will create specifically for this deployment project.

**Agent Responsibilities:**
- **Agent 1 (Development Agent)**: Creates feature branches, implements code according to the plan, creates pull requests, and addresses review feedback.
- **Agent 2 (Code Review Agent)**: Reviews pull requests for code quality, best practices, correctness, performance, and maintainability. Provides detailed feedback.
- **Agent 3 (Plan Alignment Agent)**: Reviews pull requests against this ExecPlan to ensure completeness, checks that all requirements are met, manages merge conflicts, and approves/merges when criteria are satisfied.

**Workflow Trigger:** The workflow begins when you create a new GitHub repository, push this ExecPlan to it, and provide a reference to the source notebook. The agents then work sequentially: Agent 1 develops, creates a PR, Agent 2 reviews the code, Agent 3 reviews alignment with the plan, and if all pass, Agent 3 merges. If issues are found, Agent 1 addresses feedback and the cycle repeats until completion.

## Workflow Orchestration and Agent Coordination

**Initial Trigger (Human Action - One Time):**

To start the automated workflow, you must:
1. Create a new GitHub repository (e.g., `llm-playground-app`)
2. Push this ExecPlan file to the repository's main branch
3. Provide agents with:
   - Repository URL (e.g., `https://github.com/yourusername/llm-playground-app`)
   - Source notebook path: `/Users/tempUser/Projects/ai-engineering-course/project_1/lm_playground.ipynb`
   - Branch name for main (typically `main` or `master`)

**Agent Execution Sequence:**

The workflow follows this sequence, with each agent waiting for the previous agent's checkpoint:

1. **Agent 1 (Development) starts**: 
   - Creates git work tree in temporary directory
   - Creates feature branch `feature/streamlit-app`
   - Implements code according to this ExecPlan
   - Commits and pushes feature branch
   - Creates pull request targeting main branch
   - **Checkpoint**: PR created and ready for review

2. **Agent 2 (Code Review) starts** (after Agent 1 checkpoint):
   - Reads PR diff and all changed files
   - Reviews code quality, best practices, correctness
   - Adds PR comments with feedback
   - Approves PR if code meets standards, or requests changes
   - **Checkpoint**: PR approved OR change requests provided

3. **Agent 3 (Plan Alignment) starts** (after Agent 2 checkpoint):
   - If Agent 2 requested changes: Wait for Agent 1 to address feedback
   - If Agent 2 approved: Proceed to alignment check
   - Verifies implementation matches ExecPlan requirements
   - Checks for merge conflicts and resolves if needed
   - Merges PR to main if all checks pass
   - **Checkpoint**: PR merged to main OR specific fixes requested

4. **Iteration Loop** (if fixes needed):
   - Agent 1 addresses feedback from Agent 2 or Agent 3
   - Pushes new commits to feature branch
   - Agent 2 re-reviews (if Agent 2's feedback)
   - Agent 3 re-checks alignment (if Agent 3's feedback)
   - Loop continues until all agents approve

5. **Completion**:
   - PR merged to main branch
   - Work tree cleaned up
   - Repository ready for Streamlit Community Cloud deployment

**Agent Communication Protocol:**

Agents communicate through Git and GitHub:
- **Agent 1 → Agent 2**: PR creation signals readiness for review
- **Agent 2 → Agent 1**: PR comments provide feedback
- **Agent 2 → Agent 3**: PR approval status (approved/change_requested) signals readiness
- **Agent 3 → Agent 1**: PR comments or merge decision
- **Agent 3 → Completion**: Merge commit signals workflow completion

**Work Tree Management:**

Each agent uses git work trees to avoid conflicts:
- Agent 1: Creates work tree at `/tmp/llm-playground-dev-worktree` (or configurable path)
- Agent 2: Reads PR via GitHub API or git fetch (no work tree needed for review)
- Agent 3: Uses main repository directory for merge operations

Work trees are cleaned up after successful merge or can be manually removed if workflow is interrupted.

**Error Handling and Recovery:**

If any agent fails:
- Work tree and branch state are preserved in Git
- Workflow can be resumed from last checkpoint
- Agents can re-read PR state and continue from where they left off
- No data loss occurs as all work is in Git

**Automation Requirements:**

For full automation, agents need:
- Git CLI access
- GitHub CLI (`gh`) or GitHub API access for PR operations
- Read access to source notebook path
- Write access to deployment repository
- Ability to create work trees and branches

## Plan of Work

The work involves converting the interactive playground section from a Jupyter notebook widget-based interface into a Streamlit web application, then deploying it to Streamlit Community Cloud. This will be accomplished through an automated multi-agent workflow operating on a separate GitHub repository.

**Initial Setup (Human Action Required Once):**
You will create a new GitHub repository (e.g., `llm-playground-app`) and push this ExecPlan to it. This repository will be the target for all agent work. The agents will reference the source notebook at `/Users/tempUser/Projects/ai-engineering-course/project_1/lm_playground.ipynb` or you can provide a path/URL to the notebook.

**Agent 1 (Development Agent) Workflow:**
Agent 1 will set up a git work tree in a temporary directory to work independently. It will create a feature branch (e.g., `feature/streamlit-app`), extract the core functionality from the notebook's section 5, and implement the Streamlit application. The playground section loads GPT-2 and Qwen models, implements a text generation function that supports multiple decoding strategies (greedy, top-k, top-p), and provides UI controls for prompt input, model selection, strategy selection, temperature adjustment, and max tokens. Agent 1 will preserve all this functionality while replacing `ipywidgets` with Streamlit components.

Agent 1 will create `app.py` containing the Streamlit application with proper model loading (using `@st.cache_resource` for caching), the generation function, and UI components (`st.text_area`, `st.selectbox`, `st.slider`, `st.button`). It will enhance the UI with titles, descriptions, organized layouts, and professional styling. Agent 1 will also create `requirements.txt` based on `env.yaml` dependencies and a comprehensive `README.md`. Once complete, Agent 1 will push the feature branch and create a pull request.

**Agent 2 (Code Review Agent) Workflow:**
Agent 2 will review the pull request for code quality, best practices, correctness, error handling, performance considerations, and maintainability. It will check that the code follows Python conventions, uses Streamlit appropriately, handles edge cases, and includes proper error messages. Agent 2 will provide detailed feedback as PR comments, requesting changes if issues are found, or approving if the code meets standards.

**Agent 3 (Plan Alignment Agent) Workflow:**
Agent 3 will review the pull request against this ExecPlan to ensure all requirements are met. It will verify that:
- All files specified in the plan are present (`app.py`, `requirements.txt`, `README.md`)
- The implementation matches the specifications in the "Interfaces and Dependencies" section
- All acceptance criteria from "Validation and Acceptance" can be verified
- The code structure aligns with the "Plan of Work" description

If merge conflicts arise (e.g., if the main branch changed), Agent 3 will resolve them autonomously. If all checks pass, Agent 3 will merge the PR. If issues are found, Agent 3 will request specific fixes, and Agent 1 will address them in a new commit, restarting the review cycle.

**Iteration and Completion:**
The agents will iterate until all reviews pass and the code is merged to the main branch. Once merged, the repository will be ready for Streamlit Community Cloud deployment. The final step (deployment to Streamlit Community Cloud) may require a one-time manual action to connect the repository, but the code will be fully prepared.

## Concrete Steps

**Prerequisites (Human Action - One Time Only):**

1. Create a new GitHub repository (e.g., `llm-playground-app`) for this deployment project
2. Initialize the repository with a README and this ExecPlan file
3. Provide the source notebook path: `/Users/tempUser/Projects/ai-engineering-course/project_1/lm_playground.ipynb` (or make it accessible to agents)

**Agent 1 (Development Agent) - Implementation Steps:**

All commands for Agent 1 should be run in a git work tree to avoid conflicts. The work tree will be created in a temporary directory.

**Step 1.1: Set up git work tree and feature branch**

```bash
# Clone or identify the deployment repository
REPO_URL="<your-github-repo-url>"
WORK_TREE_DIR="/tmp/llm-playground-dev-worktree"
REPO_DIR="/tmp/llm-playground-repo"

# Clone the repository if not already cloned
git clone $REPO_URL $REPO_DIR
cd $REPO_DIR

# Create a work tree for Agent 1's work
git worktree add $WORK_TREE_DIR -b feature/streamlit-app
cd $WORK_TREE_DIR
```

**Step 1.2: Read source notebook and extract section 5**

Agent 1 will read the notebook at `/Users/tempUser/Projects/ai-engineering-course/project_1/lm_playground.ipynb`, locate section 5 (starting around cell 52), and extract:
- Model loading code (cells 49-50): GPT-2 and Qwen model/tokenizer loading
- Generation function (cell 45): The `generate()` function supporting greedy, top-k, and top-p strategies
- UI logic (cell 53): The interactive playground interface using ipywidgets

**Step 1.3: Create app.py with Streamlit implementation**

Create `app.py` in the work tree root with the complete Streamlit application. Convert ipywidgets to Streamlit:
- `widgets.Textarea` → `st.text_area`
- `widgets.Dropdown` → `st.selectbox`
- `widgets.FloatSlider` → `st.slider` with `min_value`, `max_value`, `step`
- `widgets.IntSlider` → `st.slider` with `type="int"`
- `widgets.Button` → `st.button`
- `widgets.Output` → `st.empty()` or direct `st.write`/`st.markdown`

Use `@st.cache_resource` decorator on model loading functions. Structure the UI with:
- `st.title("LLM Playground")`
- `st.markdown()` for description
- `st.sidebar` for settings (model, strategy, temperature, max_tokens)
- Main area for prompt input and output display
- `st.columns` for organized layout
- Professional styling with proper spacing and formatting

**Step 1.4: Create requirements.txt**

Create `requirements.txt` with dependencies:
```
streamlit>=1.28.0
torch>=2.0.0
transformers>=4.30.0
tiktoken>=0.5.0
```

**Step 1.5: Create README.md**

Create comprehensive `README.md` with:
- App description and features
- Local setup instructions (`streamlit run app.py`)
- Deployment instructions for Streamlit Community Cloud
- Model information and performance notes
- Screenshots or usage examples (optional)

**Step 1.6: Commit and create pull request**

```bash
cd $WORK_TREE_DIR
git add app.py requirements.txt README.md
git commit -m "feat: Add Streamlit LLM Playground application

- Convert notebook section 5 to Streamlit app
- Implement model loading with caching
- Add UI controls for prompt, model, strategy, temperature, max_tokens
- Support GPT-2 and Qwen models
- Support greedy, top-k, and top-p decoding strategies"

git push origin feature/streamlit-app

# Create pull request (using GitHub CLI or API)
gh pr create --title "Add Streamlit LLM Playground App" --body "Implements the Streamlit application as specified in the ExecPlan. Ready for review."
```

**Agent 2 (Code Review Agent) - Review Steps:**

**Step 2.1: Review pull request code quality**

Agent 2 will:
- Read the PR diff and all changed files
- Check code follows Python best practices (PEP 8, proper naming, docstrings)
- Verify Streamlit usage is correct and efficient
- Check error handling (model loading failures, generation errors, invalid inputs)
- Review performance (model caching, efficient generation)
- Check for security issues (input validation, resource limits)
- Verify code is maintainable and well-structured

**Step 2.2: Provide review feedback**

Agent 2 will add PR comments for:
- Code quality issues
- Potential bugs or edge cases
- Performance improvements
- Best practice suggestions
- Missing error handling

If critical issues found, request changes. If only minor suggestions, approve with comments.

**Agent 3 (Plan Alignment Agent) - Alignment and Merge Steps:**

**Step 3.1: Review against ExecPlan**

Agent 3 will verify:
- All required files exist: `app.py`, `requirements.txt`, `README.md`
- Implementation matches "Interfaces and Dependencies" specifications
- Code structure aligns with "Plan of Work" description
- All acceptance criteria from "Validation and Acceptance" are addressable

**Step 3.2: Check for merge conflicts**

```bash
cd $REPO_DIR
git fetch origin
git checkout main
git merge origin/feature/streamlit-app --no-commit --no-ff
```

If conflicts exist, Agent 3 will resolve them by:
- Identifying conflicting sections
- Choosing appropriate resolution (typically accepting feature branch changes)
- Ensuring resolved code still meets plan requirements
- Committing the merge resolution

**Step 3.3: Merge or request fixes**

If Agent 2 approved and Agent 3 alignment check passes:
```bash
git merge origin/feature/streamlit-app
git push origin main
```

If issues found, Agent 3 will request specific fixes. Agent 1 will address feedback:
```bash
cd $WORK_TREE_DIR
# Make fixes based on review feedback
git add .
git commit -m "fix: Address review feedback"
git push origin feature/streamlit-app
```

The review cycle repeats until all agents approve.

**Step 3.4: Cleanup work tree**

After successful merge:
```bash
cd $REPO_DIR
git worktree remove $WORK_TREE_DIR
git branch -d feature/streamlit-app  # Delete local branch
```

**Final Step: Deployment to Streamlit Community Cloud (Manual One-Time Action)**

Once code is merged to main:
1. Navigate to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select repository: `llm-playground-app`
5. Branch: `main`
6. Main file: `app.py`
7. Click "Deploy"

The app is live at: [https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/](https://llm-playground-wcetd6cughskwjruzprbgp.streamlit.app/)

## Validation and Acceptance

The automated workflow is successful when:

1. **Agent 1 completes implementation**: The feature branch contains `app.py`, `requirements.txt`, and `README.md` with all required functionality. Code follows the specifications in "Interfaces and Dependencies" section.

2. **Agent 2 approves code quality**: The pull request receives approval from Agent 2 with no critical issues. Code follows best practices, handles errors appropriately, and is maintainable.

3. **Agent 3 confirms plan alignment**: Agent 3 verifies that the implementation matches this ExecPlan, all required files are present, and the code structure aligns with the plan. Merge conflicts (if any) are resolved.

4. **PR is merged to main**: The pull request is successfully merged to the main branch of the separate deployment repository.

5. **Repository is deployment-ready**: The main branch contains all files needed for deployment:
   - `app.py` with complete Streamlit application
   - `requirements.txt` with correct dependencies
   - `README.md` with comprehensive documentation

6. **Code can be tested locally** (verification step): Running `streamlit run app.py` from the repository produces a working web interface where you can:
   - Input prompts in a text area
   - Select models (GPT-2, Qwen) and strategies (greedy, top_k, top_p)
   - Adjust temperature (0.1-2.0) and max tokens (10-200)
   - Generate text that displays correctly
   - Test multiple scenarios successfully

7. **Streamlit Community Cloud deployment succeeds** (manual step): After connecting the repository to Streamlit Community Cloud, the app deploys without errors, and the build log shows successful installation of all dependencies.

8. **Live app functions correctly**: Navigating to the deployed URL shows:
   - A polished interface with clear title and description
   - All UI controls visible and functional
   - Text generation works with different models and strategies
   - Professional appearance suitable for portfolio

The automated workflow minimizes human involvement: once you create the repository and trigger the agents, they work autonomously until the code is merged and ready for deployment. The final deployment step (connecting to Streamlit Community Cloud) is a one-time manual action.

## Idempotence and Recovery

All steps are idempotent and safe to repeat:

**Agent Workflow Idempotence:**
- Git work trees can be recreated if deleted; `git worktree add` is safe to run multiple times
- Feature branches can be deleted and recreated; Agent 1 can start fresh if needed
- Pull requests can be closed and new ones created if the workflow needs to restart
- Agent 2 can re-review updated PRs; comments accumulate and can be addressed iteratively
- Agent 3 can re-check alignment after fixes; merge can be retried after conflict resolution

**Code Changes:**
- Creating `app.py` will overwrite existing files, but changes are in feature branches until merged
- `requirements.txt` updates are additive and safe
- README updates don't affect functionality

**Recovery Scenarios:**

1. **Agent 1 fails mid-implementation**: Delete the work tree and feature branch, have Agent 1 restart from Step 1.1. The repository state is unchanged.

2. **Agent 2 finds critical issues**: Agent 1 addresses feedback in new commits on the same PR. Agent 2 re-reviews. No data loss.

3. **Agent 3 finds merge conflicts**: Agent 3 resolves conflicts autonomously. If resolution fails, Agent 1 can rebase the feature branch and force-push (with caution).

4. **PR needs to be restarted**: Close the PR, delete the feature branch, have Agent 1 create a new branch and PR. Previous work is preserved in Git history.

5. **Deployment fails after merge**: Fix issues in a new feature branch (Agent 1), create new PR, repeat review cycle. Main branch can be reverted if needed.

**Workflow Interruption:**
If the automated workflow is interrupted (e.g., agent failure, network issue), it can be resumed from the last successful checkpoint:
- If Agent 1 completed: Check for existing PR, continue with Agent 2
- If Agent 2 completed: Continue with Agent 3
- If Agent 3 completed: Workflow is done, proceed to deployment

No cleanup is needed between attempts. Git work trees are temporary and can be safely removed and recreated.

## Artifacts and Notes

(To be populated with actual outputs, error messages, and evidence during implementation)

Expected file structure in the separate deployment repository after completion:
```
llm-playground-app/          # Separate GitHub repository
  ├── app.py                 # Main Streamlit application
  ├── requirements.txt       # Python dependencies
  ├── README.md             # Documentation and deployment instructions
  ├── deployment_plan.md    # This ExecPlan (copied from original location)
  └── .git/                 # Git repository metadata
```

The original project structure remains unchanged:
```
ai-engineering-course/
  └── project_1/
      ├── env.yaml              # (existing, for local conda environment)
      ├── lm_playground.ipynb   # (existing, original notebook)
      └── deployment_plan.md    # (original plan, may be copied to new repo)
```

## Interfaces and Dependencies

The Streamlit application (`app.py`) will use the following key interfaces:

**Streamlit components:**
- `streamlit` (imported as `st`) - Main Streamlit library for UI components
- `st.title()` - Display app title
- `st.markdown()` - Display formatted text
- `st.text_area()` - Multi-line text input for prompts
- `st.selectbox()` - Dropdown selector for model and strategy
- `st.slider()` - Slider input for temperature and max_tokens
- `st.button()` - Button to trigger generation
- `st.empty()` - Placeholder for dynamic content updates
- `st.cache_resource()` - Decorator to cache model loading

**Model and generation libraries:**
- `transformers.AutoModelForCausalLM` - Load pre-trained language models
- `transformers.AutoTokenizer` - Load tokenizers for models
- `torch` - PyTorch for tensor operations (models require this)

**Model specifications:**
- GPT-2 model: `"gpt2"` (loaded via `AutoModelForCausalLM.from_pretrained("gpt2")`)
- Qwen model: `"Qwen/Qwen2.5-0.5B-Instruct"` (loaded via `AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")`)

**Generation function signature:**
The `generate()` function should accept:
- `model` - The loaded model object
- `tokenizer` - The corresponding tokenizer
- `prompt` - String input text
- `strategy` - One of `"greedy"`, `"top_k"`, or `"top_p"`
- `max_new_tokens` - Integer for maximum tokens to generate
- `temperature` - Float for sampling temperature
- `top_k` - Integer for top-k sampling (when strategy is "top_k")
- `top_p` - Float for nucleus sampling (when strategy is "top_p")

And return a decoded string of generated text.

**Deployment platform:**
- Streamlit Community Cloud (https://share.streamlit.io)
- Requires GitHub repository with public access (for free tier)
- Automatically detects `requirements.txt` and installs dependencies
- Supports Python 3.8-3.11 (default is typically 3.11)

**Multi-Agent Workflow Interfaces:**

**Agent 1 (Development Agent) Interface:**
- Input: ExecPlan file, source notebook path, repository URL
- Output: Feature branch with `app.py`, `requirements.txt`, `README.md`, pull request
- Tools: Git commands, file I/O, code generation
- Checkpoint: PR created and ready for review

**Agent 2 (Code Review Agent) Interface:**
- Input: Pull request URL or branch reference
- Output: PR review comments, approval status, change requests
- Tools: Code analysis, diff reading, best practice checking
- Checkpoint: Review complete with approval or change requests

**Agent 3 (Plan Alignment Agent) Interface:**
- Input: Pull request, ExecPlan file
- Output: Alignment verification, conflict resolution, merge decision
- Tools: Plan parsing, requirement checking, Git merge operations
- Checkpoint: PR merged to main or feedback provided for iteration

**Workflow Orchestration:**
Agents operate sequentially with clear handoff points. Each agent completes its work and signals completion (via PR status, comments, or merge). The next agent begins when the previous agent's checkpoint is reached. If an agent requests changes, the workflow loops back to Agent 1 for fixes, then proceeds through the review cycle again.
