from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class StudyPlanner():
    """Study planner crew"""


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'],
            verbose=True
        )

    @task
    def resource_research(self) -> Task:
        return Task(
            config=self.tasks_config['resource_research'],
        )

    @task
    def learning_plan(self) -> Task:
        return Task(
            config=self.tasks_config['learning_plan'],
        )

    @task
    def final_study_guide(self) -> Task:
        return Task(
            config=self.tasks_config['final_study_guide'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the study planner crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
