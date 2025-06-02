
# Super class
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.person_id}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, person_id, course):
        super().__init__(name, person_id)
        self.course = course

    def display_info(self):
        super().display_info()
        print("Role: Student")
        print(f"Course: {self.course}")

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, person_id, subject):
        super().__init__(name, person_id)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print("Role: Lecturer")
        print(f"Subject: {self.subject}")

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, person_id, department):
        super().__init__(name, person_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Role: Staff")
        print(f"Department: {self.department}")


student = Student("Alice", "K123", "Computer Science")
lecturer = Lecturer("Dr. Chris", "D456", "Mathematics")
staff = Staff("Charlie", "ST789", "Administration")

# Display Information
print(" Student Details")
student.display_info()

print("\nLecturer Details")
lecturer.display_info()

print("\nStaff details")
staff.display_info()
