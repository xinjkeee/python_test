from datetime import datetime, timezone
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent, ToolNode 
from langchain.tools import tool
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, ToolMessage
from typing import TypedDict, Annotated, List
import operator

@tool
def get_current_time() -> dict:
    """Return the current UTC time in ISO‑8601 format.
    Example → {"utc": "2025‑05‑21T06:42:00Z"}"""
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {"utc": utc_now}

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]

model = ChatOllama(model="qwen3:1.7b")
tools = [get_current_time]

agent_runnable = create_react_agent(
    model=model,
    tools=tools,
    prompt="""
    You are a helpful assistant. You can access external tools by writing special commands.

Available tool:

Function: get_current_time()
Description: Returns the current UTC time in ISO-8601 format, like {"utc": "2025-05-21T06:42:00Z"}

When you need to use a tool, respond with:
TOOL_CALL: get_current_time()

Only use the 'get_current_time' tool if the user explicitly asks for the current time or a time-related query. For general greetings like "Hello", respond naturally without using tools. Do not make up the answer yourself.
"""
)

tool_node = ToolNode(tools)

def should_continue(state: AgentState):
    last_message = state['messages'][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools" 
    return END

graph = StateGraph(AgentState)

graph.add_node("agent", agent_runnable)
graph.add_node("tools", tool_node)

graph.set_entry_point("agent")

graph.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        END: END
    }
)

graph.add_edge("tools", "agent")
app = graph.compile()

def get_graph():
    return app
