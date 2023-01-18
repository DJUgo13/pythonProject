class Person:
    def __init__(self, fullname, age, is_maried):
        self.fullname = fullname
        self.age = age
        self.is_maried = is_maried

    def introduce_myself(self):
        print(f'name:{self.fullname}\nage:{self.age}\nis maried:{self.is_maried}')


Jojo = Person('Jotaro Kujo', 16, 'NO')
Jojo.introduce_myself()


class Student(Person):

    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def avarage(self):
        c = 0
        s = 0
        for item in self.marks.values():
            c += 1
            s += item
        print(round(s / c, 1))


class Teacher(Person):
    salary = 1500

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def cash(self):
        if self.experience > 3:
            salary_new = self.salary + (self.salary / 100 * 5)
            print(salary_new)
        else:
            print(self.salary)


Tatiana = Teacher('Tatiana', 36, 'yes', 11)
Tatiana.introduce_myself()
Tatiana.cash()
student = []


def create_students():
    student1 = Student('Bogdan', 19, 'yes', marks={
        'algebra': 5,
        'english': 3,
        'python': 4
    })
    student.append(student1)
    student2 = Student('Alan', 21, 'no', marks={
        'python': 5,
        'algebra': 5,
        'english': 3
    })
    student.append(student2)
    student3 = Student('Mark', 25, 'yes', marks={
        'english': 4,
        'python': 5,
        'algebra': 4
    })
    student.append(student3)


create_students()
for i in student:
    i.introduce_myself()
    i.avarage()
