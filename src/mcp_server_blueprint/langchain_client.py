import asyncio

from langchain.mcp import MCPAdapter

mcp_adapter = MCPAdapter("http://127.0.0.1:8000/mcp")

async def main():

    async with mcp_adapter:
        tools = await mcp_adapter.list_tools()

        for tool in tools:
            print(f"tool's name: {tool.name} tool's description: {tool.description}")

if __name__ == "__main__":
    asyncio.run(main())
        