# Task: Print student details using **kwargs
def student_info(**details):
    print("Student Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Ankaj", age=36, course="Python")
student_info(name="Riya", grade="A", city="Delhi")
