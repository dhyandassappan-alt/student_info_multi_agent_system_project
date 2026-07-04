from fastmcp import Client
import asyncio

client = Client("server.py")

async def research_student(name):
    async with client:
        result = await client.call_tool(
            "get_student_by_name",
            {"name": name}
        )

        return result.content[0].text