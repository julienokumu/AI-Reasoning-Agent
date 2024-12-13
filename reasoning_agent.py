from phi.agent import Agent
from phi.model.openai import OpenAIChat
import os

api_key = os.environ["API_KEY"]
# temporary fix for updating the OPENAI_API_KEY
# proper fix coming soon
os.environ["OPENAI_API_KEY"] = api_key

reasoning_agent = Agent(
    name="Reasoning Agent",
    model=OpenAIChat(
        id="gpt-4o",
        base_url="https://models.inference.ai.azure.com",
        api_key=api_key
    ),
    markdown=True,
    reasoning=True,
    structured_outputs=True,
    instructions=[
        "Start by giving a philosophical quote by Franz Kafka in relation to the question"
    ]
)

task = (
    "There are 4 rats in a kitchen"
    "Safely remove all 4 rats from the kitchen without alerting the other rats"
    "Provide a step-by-step solution and show the solution as an ASCII diagram"
)

reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
