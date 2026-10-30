import asyncio

from fastmcp import Client
from fastmcp.exceptions import ToolError

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

        print("testing update normally")
        result = await client.call_tool(
            "update_task_status",
            {
                "task_id": result2.data[0]["task_id"],
                "status": "in_progress"
            }
        )

        print(result.data)
        print("testing update with wrong ID")
        result = await client.call_tool(
                    "update_task_status",
                    {
                        "task_id": '5e6a57eb-607b-40ea-8c7c-0dd8b4558478',
                        "status": "in_progress"
                    }
                )
        
        print(result.data)

        print("testing update with wrong status")
        try:
            result = await client.call_tool(
                        "update_task_status",
                        {
                            "task_id": '5e6a57eb-607b-40ea-8c7c-0dd8b4558478',
                            "status": "working"
                        }
                    )
            print(result.data)
        except ToolError as e:
            print(f"Error: {e}")
        
    return tools


if __name__ == "__main__":
    asyncio.run(get_tools_from_server())