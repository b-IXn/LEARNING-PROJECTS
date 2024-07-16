class Student:
    def __init__(self,name,id_no,grade,faculty):
        self.name = name
        self.id_no = id_no
        self.grade = grade
        self.faculty = faculty

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_no}, Grade: {self.grade}, Faculty: {self.faculty}"

class studentManagement:
    def __init__(self):
        self.student = []

    def addStudent(self,name,id_no,grade,faculty):
        student = Student(name,id_no,grade,faculty)
        self.student.append(student)
        print(f'student added! Name: {name}, ID: {id_no}, Grade: {grade}, Faculty: {faculty}')
    def updateStudent(self,name,new_grade,new_faculty):
        for student in self.student:
            if student.name == name:
                student.grade = new_grade
                student.faculty = new_faculty
                return
        else:
            print('student not found')



    def viewStudent(self):
        for student in self.student:
            print(student)


def main():
    sm = studentManagement()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. View Students")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input('enter the name of student you wanna add: ')
            id_no = input('enter the students id: ')
            grade = input('enter the students grade: ')
            faculty = input('enter the students faculty: ')
            sm.addStudent(name,id_no,grade,faculty)

        elif choice == '2':
            name = input('enter the name of student you wanna uodate: ')
            new_grade = input(f'enter new grade of {name}: ')
            new_faculty = input(f'enter new faculty of {name}: ')
            sm.updateStudent(name,new_grade,new_faculty)

        elif choice == '3':
            sm.viewStudent()

        elif choice == '4':
            print('exiting sms')

        else:
            print('invalid choice')
            break

if __name__ == '__main__':
    main()
