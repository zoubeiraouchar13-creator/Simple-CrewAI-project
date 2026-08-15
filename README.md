# CrewAI Tutorial

Welcome to the Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-1.14.5-purple)
![LangChain](https://img.shields.io/badge/LangChain-1.4.0-orange)
![LangSmith](https://img.shields.io/badge/LangSmith-0.8.5-yellow)
![Groq](https://img.shields.io/badge/Groq-0.37.1-darkviolet)
![OpenAI](https://img.shields.io/badge/OpenAI-2.37.0-lightblue)
![Transformers](https://img.shields.io/badge/Transformers-5.7.0-red)
![Torch](https://img.shields.io/badge/Torch-2.11.0-darkred)
![Scikit‑Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-green)
![Pandas](https://img.shields.io/badge/Pandas-3.0.2-blue)
![ChromaDB](https://img.shields.io/badge/ChromaDB-1.1.1-lightgrey)
![LanceDB](https://img.shields.io/badge/LanceDB-0.30.0-brown)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.47.0-black)
![Starlette](https://img.shields.io/badge/Starlette-1.0.0-darkblue)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-1.34.1-cyan)
![License](https://img.shields.io/badge/License-CC_BY_NC-blue)

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/latest_ai_flow/config/agents.yaml` to define your agents
- Modify `src/latest_ai_flow/config/tasks.yaml` to define your tasks
- Modify `src/latest_ai_flow/crew.py` to add your own logic, tools and specific args
- Modify `src/latest_ai_flow/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your flow and begin execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the latest-ai-flow Flow as defined in your configuration.

This example, unmodified, will run a content creation flow on AI Agents and save the output to `output/post.md`.

## Understanding Your Crew

The latest-ai-flow Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the {{crew_name}} Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
