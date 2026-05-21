from crewai_tools import SerperDevTool
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

#For local testing, you can use Ollama to run the model locally. 
# Make sure to set up your .env file with the appropriate values for MODEL and API_BASE.
llm = LLM(
    model="ollama/qwen2.5:14b",
    base_url="http://localhost:11434"
)

@CrewBase
class ResearchCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            llm=llm,
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)

@CrewBase
class ResearchCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"], tools=[SerperDevTool()], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, 
                    tasks=self.tasks, 
                    process=Process.sequential, 
                    memory = False,
                    embedder={
                        "provider": "ollama",
                        "config": {"model_name": "mxbai-embed-large"}
                    },
                    verbose=True)