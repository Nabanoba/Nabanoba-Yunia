class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

class Lecturer(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

class Staff(Person):
    def __init__(self, name, age, gender, staff_id, position):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Position: {self.position}")

def input_student():
    print("Enter Student Details:")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    student_id = input("Student ID: ")
    course = input("Course: ")
    return Student(name, age, gender, student_id, course)

def input_lecturer():
    print("Enter Lecturer Details:")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    employee_id = input("Employee ID: ")
    department = input("Department: ")
    return Lecturer(name, age, gender, employee_id, department)

def input_staff():
    print("Enter Staff Details:")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    staff_id = input("Staff ID: ")
    position = input("Position: ")
    return Staff(name, age, gender, staff_id, position)

def display_all(person_list):
    if not person_list:
        print("No records found.")
        return
    for person in person_list:
        print("-" * 20)
        person.display_info()

def display_by_type(person_list, cls):
    filtered = [p for p in person_list if isinstance(p, cls)]
    if not filtered:
        print(f"No records found for {cls.__name__}.")
        return
    for person in filtered:
        print("-" * 20)
        person.display_info()

def main():
    person_list = []

    while True:
        print("\n--- University System Menu ---")
        print("1. Add Student")
        print("2. Add Lecturer")
        print("3. Add Staff")
        print("4. Display All")
        print("5. Display Students")
        print("6. Display Lecturers")
        print("7. Display Staff")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            student = input_student()
            person_list.append(student)
            print("Student added successfully.")
        elif choice == '2':
            lecturer = input_lecturer()
            person_list.append(lecturer)
            print("Lecturer added successfully.")
        elif choice == '3':
            staff = input_staff()
            person_list.append(staff)
            print("Staff added successfully.")
        elif choice == '4':
            print("\nAll Records:")
            display_all(person_list)
        elif choice == '5':
            print("\nStudents:")
            display_by_type(person_list, Student)
        elif choice == '6':
            print("\nLecturers:")
            display_by_type(person_list, Lecturer)
        elif choice == '7':
            print("\nStaff:")
            display_by_type(person_list, Staff)
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 8.")

if __name__ == "__main__":
    main()
