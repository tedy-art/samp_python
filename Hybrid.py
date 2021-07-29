#hybrid Inheritance
class School:
    def func1(self):
        print("This function is in School.")

class Student1(School):
    def func2(self):
        print("This function is in student 1.")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1,School):
    def func4(self):
        print("This function is in student 3.")

ob1=Student3()
ob1.func1()
ob1.func4()
ob1.func2()