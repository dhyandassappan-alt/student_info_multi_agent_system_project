import json
from fastmcp import FastMCP

# Create MCP Server
mcp = FastMCP("Student Information Server")

# Load student data from JSON
with open("data/students.json", "r") as file:
    students = json.load(file)

# Tool 1 - Get all students
@mcp.tool
def get_all_students():
    """
    Returns all students.
    """
    return students

# Tool 2 - Get college name
@mcp.tool
def get_college_name():
    """
    Returns the college name.
    """
    return "Don Bosco College, Panjim"

# Tool 3 - Get course
@mcp.tool
def get_course():
    """
    Returns the course name.
    """
    return "BCA"

# Tool 4 - Get total student count
@mcp.tool
def get_student_count():
    """
    Returns total number of students.
    """
    return len(students)

# Tool 5 - Get director
@mcp.tool
def get_director():
    """
    Returns the director's name.
    """
    return "Dr. Shantanu"

# Tool 6 - Search student by name
@mcp.tool
def get_student_by_name(name: str):
    """
    Returns student details by name.
    """
    for student in students:
        if student["name"].lower() == name.lower():
            return student

    return "Student not found."

# Run MCP Server
if __name__ == "__main__":
    mcp.run()