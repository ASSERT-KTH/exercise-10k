## Exercise
Write a program to create a student grades system where students can be added, removed, and their grades can be updated.

## Reference Solution
```python
class Student:
    """Represents a student with a name and grades."""
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """Adds a grade for a subject."""
        self.grades[subject] = grade

    def update_grade(self, subject, grade):
        """Updates a grade for a subject."""
        if subject in self.grades:
            self.grades[subject] = grade
        else:
            print("Subject not found.")

    def remove_grade(self, subject):
        """Removes a grade for a subject."""
        if subject in self.grades:
            del self.grades[subject]
        else:
            print("Subject not found.")

    def display_grades(self):
        """Displays all grades for the student."""
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")


class StudentGradesSystem:
    """Manages a collection of students and their grades."""
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        """Adds a new student."""
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student '{name}' added successfully.")
        else:
            print("Student already exists.")

    def remove_student(self, name):
        """Removes a student."""
        if name in self.students:
            del self.students[name]
            print(f"Student '{name}' removed successfully.")
        else:
            print("Student not found.")

    def update_student_grade(self, name, subject, grade):
        """Updates a grade for a student."""
        if name in self.students:
            self.students[name].update_grade(subject, grade)
        else:
            print("Student not found.")

    def add_student_grade(self, name, subject, grade):
        """Adds a grade for a student."""
        if name in self.students:
            self.students[name].add_grade(subject, grade)
        else:
            print("Student not found.")

    def remove_student_grade(self, name, subject):
        """Removes a grade for a student."""
        if name in self.students:
            self.students[name].remove_grade(subject)
        else:
            print("Student not found.")

    def display_student_grades(self, name):
        """Displays all grades for a student."""
        if name in self.students:
            print(f"Grades for {name}:")
            self.students[name].display_grades()
        else:
            print("Student not found.")

    def display_all_students(self):
        """Displays all students."""
        print("All Students:")
        for student in self.students.keys():
            print(student)


def main():
    grades_system = StudentGradesSystem()

    while True:
        print("\nStudent Grades System Menu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Add Grade for Student")
        print("4. Update Grade for Student")
        print("5. Remove Grade for Student")
        print("6. Display Grades for Student")
        print("7. Display All Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grades_system.add_student(name)
        elif choice == "2":
            name = input("Enter student name: ")
            grades_system.remove_student(name)
        elif choice == "3":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            grades_system.add_student_grade(name, subject, grade)
        elif choice == "4":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            grades_system.update_student_grade(name, subject, grade)
        elif choice == "5":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grades_system.remove_student_grade(name, subject)
        elif choice == "6":
            name = input("Enter student name: ")
            grades_system.display_student_grades(name)
        elif choice == "7":
            grades_system.display_all_students()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

## Generated Output
```
Student Grades System Menu:
1. Add Student
2. Remove Student
3. Add Grade for Student
4. Update Grade for Student
5. Remove Grade for Student
6. Display Grades for Student
7. Display All Students
8. Exit
Enter your choice: Invalid choice. Please try again.

Student Grades System Menu:
1. Add Student
2. Remove Student
3. Add Grade for Student
4. Update Grade for Student
5. Remove Grade for Student
6. Display Grades for Student
7. Display All Students
8. Exit
Enter your choice: 
Traceback (most recent call last):
  File "/tmp/tmpwrosqgfj.py", line 136, in <module>
    main()
  File "/tmp/tmpwrosqgfj.py", line 102, in main
    choice = input("Enter your choice: ")
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
