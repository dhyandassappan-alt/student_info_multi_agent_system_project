import json


def create_report(student_data):

    student = json.loads(student_data)

    report = f"""
__________________________________
        STUDENT REPORT
__________________________________

Name      : {student['name']}
Course    : {student['course']}
Semester  : {student['semester']}
__________________________________

"""

    return report


if __name__ == "__main__":

    sample = '{"id":1,"name":"dhyan","course":"BCA (AI & ML)","semester":5}'

    print(create_report(sample))