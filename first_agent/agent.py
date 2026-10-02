from google.adk.agents import Agent

from first_agent.tools import people_count

root_agent = Agent(
    name="first_agent",
    description="This is the first agent",
    model="gemini-3.6-flash",
    instruction=""" 
        You are a helpful assistant that gathers information about an event booking. You will ask the user for the number of people they are looking to book for and provide them with a list of available options based on their input.
    """,
    tools=[people_count]
)