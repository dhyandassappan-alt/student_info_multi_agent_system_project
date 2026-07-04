from fastmcp import Client
import asyncio

client = Client("server.py")


async def main():
    async with client:

        while True:
            question = input("\nAsk me something (type 'exit' to quit): ").lower()

            if question == "exit":
                break

            elif "college" in question:
                result = await client.call_tool("get_college_name")
                print(result.content[0].text)

            elif "course" in question:
                result = await client.call_tool("get_course")
                print(result.content[0].text)

            elif "director" in question:
                result = await client.call_tool("get_director")
                print(result.content[0].text)

            elif "student" in question and "count" in question:
                result = await client.call_tool("get_student_count")
                print(result.content[0].text)

            elif "all students" in question:
                result = await client.call_tool("get_all_students")
                print(result.content[0].text)

            elif question.startswith("student "):
                name = question.replace("student", "").strip()

                result = await client.call_tool(
                    "get_student_by_name",
                    {"name": name}
                )

                print(result.content[0].text)

            else:
                print("Sorry, I don't understand that question.")


asyncio.run(main())