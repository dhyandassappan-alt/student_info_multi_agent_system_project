import asyncio

from research_agent import research_student
from writer_agent import create_report
from reviewer_agent import review_report


async def main():

    print("=" * 50)
    print("      STUDENT INFORMATION MULTI-AGENT SYSTEM")
    print("=" * 50)

    while True:

        student = input("\nEnter student name (or 'exit'): ")

        if student.lower() == "exit":
            break

        print("\n Research Agent")
        data = await research_student(student)

        print(data)

        print("\n Writer Agent")

        report = create_report(data)

        print(report)

        print("\n Reviewer Agent")

        review_report(report)


asyncio.run(main())