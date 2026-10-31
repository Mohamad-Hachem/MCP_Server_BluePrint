import asyncio
from uuid import uuid4

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

mcp_adapter = MCPAdapter("http://127.0.0.1:8000/mcp")

async def main():

    async with mcp_adapter:
        tools = await mcp_adapter.list_tools()

        for tool in tools:
            print(f"tool's name: {tool.name} tool's description: {tool.description}")

        agent = create_agent(
            model="gpt-6-luna",
            tools=tools,
            system_prompt="you are a helpful task management assistant"
        )

        result = await agent.ainvoke({"messages" : [HumanMessage(content="Find the task titled 'Prepare MCP Demo Slides' in my database and change its status to 'in_progress'. " \
        "Then retrieve the tasks again to verify the change. Do not create any new tasks.")]})

        # tool inspection
        
        for message in result["messages"]:
            for tool_call in getattr(message, "tool_calls", []):
                print("Tool called:", tool_call["name"])
                print("Arguments:", tool_call["args"])

        print(result["messages"][-1].content)

async def main2():

    async with mcp_adapter:
        tools = await mcp_adapter.list_tools()

        agent = create_agent(
            model="gpt-6-luna",
            tools=tools,
            system_prompt="you are a helpful task management assistant",
            checkpointer=InMemorySaver()
        )

        config = {"configurable": {"thread_id": str(uuid4())}}
        human_question = "can you please help me"

        while human_question != "q":

            result = await agent.ainvoke({"messages" : [HumanMessage(content=human_question)]},config=config)

            print(result["messages"][-1].text)

            human_question = input("please ask your question or type q to exit:\n")



if __name__ == "__main__":
    asyncio.run(main2())
        