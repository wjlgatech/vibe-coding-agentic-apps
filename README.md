# Vibe Coding Agentic Apps

A modular, extensible framework empowering business owners, product managers, and citizen developers to design, create, and deploy full agentic applications entirely through natural conversation—whether by text, voice, reference images, or example workflows.

## Table of Contents
- [Project Overview](#project-overview)  
- [Key Features](#key-features)  
- [Conversational Design Interface](#conversational-design-interface)  
- [Architecture Overview](#architecture-overview)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
  - [Clone & Submodules](#clone--submodules)  
  - [Python Environment](#python-environment)  
- [Configuration](#configuration)  
- [Usage](#usage)  
  - [Interactive Chat UI](#interactive-chat-ui)  
  - [Voice-Activated Mode](#voice-activated-mode)  
  - [Image & Workflow References](#image--workflow-references)  
- [Directory Structure](#directory-structure)  
- [Examples](#examples)  
- [Development & Testing](#development--testing)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)
- [References](#references) 

## Project Overview  
Vibe Coding Agentic Applications transforms software development into a natural dialogue. Non-technical stakeholders can specify features, sketch workflows, or upload reference images—and our multi-agent system handles planning, code generation, testing, and deployment.

## Key Features  
- **Conversational No-Code Interface**: Build agents by chatting in plain language.  
- **Multi-Modal Input**: Support for text prompts, voice commands, reference images, and example workflow files.  
- **Multi-Agent Orchestration**: Specialized agents for planning, codegen, QA, integration, and documentation.  
- **A2A Protocol**: Expose agents as microservices for hybrid workflows in LangGraph, n8n, or OpenAI SDK.  
- **Memory & Context**: Retain conversation, project state, and user preferences for seamless session continuity.  
- **Built-In CI/CD**: Automated linting, testing, and packaging for reliable deployments.  

## Conversational Design Interface  
Business owners and product managers can:
- Describe new features: “Create a shopping-cart agent that suggests upsells.”  
- Walk through flows: “Here’s a diagram—generate the code pipeline to implement it.”  
- Show reference images: “Use this UI mockup to scaffold the frontend.”  
- Speak commands hands-free: “Deploy my latest agents to Cloud Run.”  

All without writing a single line of code.

## Architecture Overview  
Agents communicate through a central coordinator, leveraging:
1. **Human–AI Interface** (`src/interface/`)  
2. **Agentic Orchestration** (`src/orchestration/`)  
3. **Execution & Memory** (`src/agents/` + `src/memory/`)  
4. **Tool Integrations** (`src/tools/`)  

## Prerequisites  
- Git ≥ 2.30  
- Python 3.10 or 3.11  
- Docker (for containerized runs)  
- Google Cloud credentials (for Vertex AI or Cloud Run deployments)

## Installation  

### Clone & Submodules  
```bash
git clone git@github.com:/vibe-coding-agentic-applications.git
cd vibe-coding-agentic-applications
git submodule add https://github.com/google/agent-development-kit.git src/google-adk
git submodule add https://github.com/google/agent-development-kit-samples.git src/google-adk-examples
git submodule update --init --recursive
```

### Python Environment  
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e src/google-adk/
```

## Configuration  
1. Copy `config/env.example` → `.env` and populate credentials:  
   ```ini
   GOOGLE_APPLICATION_CREDENTIALS=path/to/creds.json
   AGENT_CONFIG_PATH=config/agent_config.yaml
   LOGGING_CONFIG=config/logging.yaml
   ```
2. Edit `config/agent_config.yaml` to register agents and conversational prompts.  
3. Customize `config/logging.yaml` for preferred log formats and levels.

## Usage  

### Interactive Chat UI  
Launch the text-based interface for step-by-step agent creation:  
```bash
bash scripts/run_local.sh
# Then navigate to http://localhost:8000/chat
```
Type or paste natural-language requirements; the system generates code, tests, and deployment manifests automatically.

### Voice-Activated Mode  
Enable hands-free design via microphone:  
```bash
export ENABLE_VOICE=true
bash scripts/run_local.sh
```
Speak your task—“Build a ticket-booking agent with calendar integration”—and watch as agents execute.

### Image & Workflow References  
Drag-and-drop UI mockups or upload BPMN/JSON workflows directly into the chat. Agents parse visual inputs and scaffold corresponding modules.

## Directory Structure  
```
vibe-coding-agentic-applications/
├── config/                  # YAML and .env templates  
├── deployments/             # Docker, Kubernetes, Cloud Run manifests  
├── docs/                    # Architecture and API reference  
├── infra/                   # Terraform modules, monitoring configs  
├── scripts/                 # Setup, local run, CI/CD helpers  
├── src/                     # Core application code  
│   ├── agents/              # Agent implementations  
│   ├── interface/           # NLU, dialogue & multimodal handlers  
│   ├── memory/              # Context & knowledge stores  
│   ├── orchestration/       # Coordinator & adapters  
│   ├── tools/               # Encapsulated tool integrations  
│   └── utils/               # Logging, config loader, metrics  
├── tests/                   # Unit/integration tests  
├── examples/                # Conversation-driven workflow demos  
└── README.md                # This file  
```

## Examples  
- `examples/simple_code_generation.py`: Chat-driven codegen demo  
- `examples/multi_agent_pipeline.py`: End-to-end planning → code → QA  
- `examples/n8n_integration_workflow.json`: Sample visual workflow for no-code automation  

## Development & Testing  
1. Activate virtual environment.  
2. Run linting and tests:  
   ```bash
   flake8 src tests
   pytest --maxfail=1 --disable-warnings -q
   ```

## Contributing  
Contributions welcome via pull requests. Please review [docs/api_reference.md](docs/api_reference.md) for coding standards, branch strategy, and PR guidelines.

## License  
Apache 2.0 License. See [LICENSE](LICENSE) for details.

## Contact  
Maintained by the Vibe Coding Agents Team  
- GitHub: [@vibe-coding-agentic-apps](https://github.com/wjlgatech/vibe-coding-agentic-apps)  
- Email: wjlgatech@gmail.com

## References

[1] https://convin.ai/blog/conversational-voice-ai-platform

[2] https://www.reddit.com/r/nocode/comments/12g10kx/is_there_a_nocode_platform_that_allows_users_to/

[3] https://www.botstacks.ai/blog/7-conversation-design-hurdles-solved-by-no-code-chatbots

[4] https://www.sopranodesign.com/communications-platform-as-a-service-cpaas/conversational-ai-chatbot/

[5] https://stackoverflow.com/questions/52528952/running-tests-against-code-examples-in-a-readme-md

[6] https://www.verloop.io/blog/cx-automation/

[7] https://www.nocobase.com/en/blog/the-top-12-open-source-no-code-tools-with-the-most-github-stars

[8] https://denser.ai/blog/no-code-chatbot/

[9] https://chatling.ai

[10] https://zapier.com/blog/best-no-code-app-builder/
