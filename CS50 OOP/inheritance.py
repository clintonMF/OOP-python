class Wizard:
    
    def __init__(self, name):
        self.name = name

class Student(Wizard):
    
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        
class Teacher(Wizard):
    
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("clinton")
student = Student("student")
teacher = Teacher("teacher")

# make this looks more reasonable