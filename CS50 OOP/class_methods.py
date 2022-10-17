import random

class Hat:
    
    hats = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(f"{name} from {random.choice(cls.hats)}")

def run_hat():
    Hat.sort("clinton")

# The previous code written in student.py can be refined to a single class
# using class methods

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)
    
    def __str__(self) -> str:
        return "< name: %s, house: %s >"%(self.name,self.house)
def student():
    """This code is used to run the code in the Student class"""
    student = Student.get()
    print(student)
    
if __name__ == '__main__':
    student()
    # run_hat()
        