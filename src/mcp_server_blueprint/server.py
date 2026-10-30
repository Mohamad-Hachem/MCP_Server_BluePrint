from uuid import uuid4

from fastmcp import FastMCP

mcp = FastMCP("MCP Server ACL")

tasks = []

@mcp.tool(name="create_task",description="This tool is created to create new tasks")
def create_task(title:str, priority:str="medium", description:str="") -> dict:
    """This function is created to be used as a tool in our server. it creates
       the new todo task to be done later
    """
    task_id = str(uuid4())
    status = "todo"

    task =  {"task_id":task_id, "title":title, "description":description, "status": status, "priority": priority}
    tasks.append(task)

    return task

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
