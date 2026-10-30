from uuid import uuid4

from fastmcp import FastMCP

mcp = FastMCP("MCP Server ACL")

tasks = []

@mcp.tool(name="create_task",description="This tool is created to create new tasks")
def create_task(title:str, priority:str="medium", description:str="") -> dict:
    """
    This function is created to be used as a tool in our server. it creates
    the new todo task to be done later
    """
    task_id = str(uuid4())
    status = "todo"

    task =  {"task_id":task_id, "title":title, "description":description, "status": status, "priority": priority}
    tasks.append(task)

    return task

@mcp.tool(name="list_tasks", description="this tool provide all the list of tasks that exsists in our database")
def list_tasks() -> list[dict]:
    """
    This function return all the tasks present in our database
    """
    return tasks



if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
