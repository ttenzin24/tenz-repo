class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def jump(self):
        print(f"{self.name} is jumping.")

    def kick(self):
        print(f"{self.name} is kicking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def code(self):
        print(f"{self.name} is coding.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def decode(self):
        print(f"{self.name} is decoding.")


# Creating objects
teacher1 = Teacher("Boo", 23, "CID:12007003456", "commerce", 50000, "Accounce", "Rookie Teacher")
student1 = Student("Hamper", 19, "CID:89076", "S823", "Nursing", 2, 2.8)

# Testing behaviors
teacher1.kick()
teacher1.eat()
teacher1.teach()
student1.code()
student1.decode()
