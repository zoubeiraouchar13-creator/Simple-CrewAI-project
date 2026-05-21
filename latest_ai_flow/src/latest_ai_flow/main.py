from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from latest_ai_flow.crews.content_crew.content_crew import ResearchCrew

class ResearchFlowState(BaseModel):
    topic: str = ""
    report: str = ""

class LatestAiFlow(Flow[ResearchFlowState]):
    @start()
    def prepare_topic(self):
        self.state.topic = "AI Agents"

    @listen(prepare_topic)
    def run_research(self):
        result = ResearchCrew().crew().kickoff(inputs={"topic": self.state.topic})
        self.state.report = result.raw

def kickoff():
    LatestAiFlow().kickoff()