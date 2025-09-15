"Student Management System"


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")


class GraduateStudent(Student):
    def __init__(self, name, age, grades, research_topic):
        super().__init__(name, age, grades)
        self.research_topic = research_topic

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")

def main():
    student = Student("John", 20, [85, 90, 88])
    grad_student = GraduateStudent("Alice", 25, [90, 92, 95], "Artificial Intelligence")

    print("=== Student Info ===")
    student.display_info()
    print("\n=== Graduate Student Info ===")
    grad_student.display_info()

if __name__ == "__main__":
    main()