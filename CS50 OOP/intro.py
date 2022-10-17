# keeping this to make me recall that you don't have to define the constructor of a class

class Student:
    ...

def student():
    student = get_student()
    print(f"{student.name} lives at {student.house}")
    
def get_student():
    student = Student()
    student.name = input("name: ")
    student.house = input("house: ")
    
    return student
    
student()