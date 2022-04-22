
# classes as boilerplates for objects

class Person():
    # the method that runs as soon as you create a class
    def __init__(self, name, age, color): #self, we are passing this instance of this class to this __init__() function
        # create some attributes for person class
        self.name = name
        self.age = age
        self.color = color
        
    def year_of_birth(self):
        return 2022-self.age
        
    # date of birth method
    def fault_year_of_birth(self):
        return 2022-self.age
        
    # projected age
    def projected_age(self, years=5):
        return self.age+years


new_person = Person('elon musk', 38, 'blue')

print(new_person.color)
print(new_person.year_of_birth())
print(new_person.projected_age(years=100))