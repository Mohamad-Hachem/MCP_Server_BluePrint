import asyncio

from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def get_tools_from_server():
    async with client:
        tools = await client.list_tools()

        # printing tools
        for tool in tools:
            print(tool.name)

        # calling tool create_task
        result = await client.call_tool(
            "create_task",
            {
            "title": "Record MCP Tutorial",
            "priority": "high",
            "description": "Create a YouTube tutorial about MCP"
            }
        )

        print(result.data)


        result2 = await client.call_tool(
            "list_tasks"
        )
        print(result2.data)

    return tools


if __name__ == "__main__":
    asyncio.run(get_tools_from_server())