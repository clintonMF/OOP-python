class Student:
    
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
        
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") 
        self._house = house
                
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    
def get_student():
    name = input("name: ")
    house = input("house: ")
    student = Student(name, house)
    
    return student

def main():
    student = get_student()
    student.house = "Ravenclaw"
    print(student)
    
main()