def review_report(report):

    print("\n Reviewer Agent is checking the report...\n")

    checks = []

    if "Name" in report:
        checks.append("Name Found")

    if "Course" in report:
        checks.append("Course Found")

    if "Semester" in report:
        checks.append("Semester Found")

    if len(checks) == 3:
        status = "APPROVED"
    else:
        status = "REJECTED"

    print("\n".join(checks))
    print("\nStatus :", status)


if __name__ == "__main__":

    sample_report = """
__________________________________
      STUDENT REPORT
__________________________________

Name      : dhyan
Course    : BCA (AI & ML)
Semester  : 5
"""
    review_report(sample_report)