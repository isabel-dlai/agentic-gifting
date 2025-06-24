from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

brainstormer = Agent(
    role="Gift Brainstormer",
    goal="Brainstorm a large list of good gifts based on {description}",
    backstory="You're an expert in choosing interesting, well-suited "
              "gifts for people that fit their personality and are well "
              "received. You're observant, sophisticated, yet down to earth.",
    allow_delegation=False,
	verbose=True
)

selector = Agent(
    role="Gift Selector",
    goal="Choose a gift from among the specified gifts to give to the person.",
    backstory="",
    allow_delegation=False,
    verbose=True
)

list_of_gifts = Task(
    description=(
        "Brainstorm a list of gifts using the provided {description}"
    ),
    expected_output="A comprehensive list of gifts",
    agent=brainstormer
)

final_gift = Task(
    description=(
        "From among the provided list of gifts, select a single gift to give to the person."
    ),
    expected_output="A single gift",
    agent=selector
)

crew = Crew(
    agents=[brainstormer, selector],
    tasks=[list_of_gifts, final_gift]
)

result = crew.kickoff(inputs={"description": "This person loves socks, candles, traveling, and anime."})

print(result)
