from langgraph.graph import StateGraph
from nodes.input_node import input_node
from nodes.processing_node import processing_node
from nodes.recommendation_node import recommendation_node
from typing import TypedDict, List, Any


class AgentState(TypedDict, total=False):
    input_data: dict
    metrics: dict
    summary: dict


def build_agent():
    builder = StateGraph(AgentState)

    builder.add_node("input", input_node)
    builder.add_node("process", processing_node)
    builder.add_node("recommend", recommendation_node)

    builder.set_entry_point("input")
    builder.add_edge("input", "process")
    builder.add_edge("process", "recommend")

    builder.set_finish_point("recommend")

    return builder.compile()


if __name__ == "__main__":
    agent = build_agent()

    sample_data = {
        "today": {"revenue": 1200, "cost": 800, "customers": 40},
        "yesterday": {"revenue": 1000, "cost": 600, "customers": 50},
    }

    result = agent.invoke({"input_data": sample_data})
    print(result["summary"])
