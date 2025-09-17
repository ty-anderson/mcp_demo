"""
MCP Demo
--------

This is a demo of how to use LangChain with MCP.

To run this demo, first install the dependencies: ``uv add langchain-anthropic python-dotenv langgraph``


"""
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

# 1. Define your LLM
llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0  # tells the llm how varied responses should be. 0=always same answer (highest probability).
)

# 2. Define a tool
@tool
def get_weather(city: str) -> str:
    """Gets the weather for a given city."""
    print(f"[Tool] Getting weather for {city}")
    return f"The weather in {city} is sunny."

@tool
def get_population(city: str) -> str:
    """Gets the population of a given city."""
    return f"The population of {city} is about 3 million."


@tool
def get_latitude_and_longitude(city: str) -> str:
    """Gets the latitude and longitude of a given city."""
    return f"The population of {city} is about 3 million."



# 3. Create the agent (LangGraph style)
agent = create_react_agent(llm, [get_weather, get_population, get_latitude_and_longitude], debug=True)

# 4. Invoke it
result = agent.invoke({"messages": [{"role": "user", "content": "What is the weather like in San Francisco?."}]})

# Get the last message
last_message = result["messages"][-1]
print(last_message.content)
