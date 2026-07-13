class person:
    def __init__(self):
        pass
    def acceptPerson(self):
        self.name=input('Enter name\n')
        self.gender=input('Enter Gender\n')
        self.height=float(input('Enter height\n'))
        self.weight=float(input('Enter weight\n'))
    def displayPerson(self):
        print(f'Name:\t{self.name}\n')
        print(f'Gender:\t{self.gender}\n')
        print(f'Height:\t{self.height}\n')
        print(f'Weight:\t{self.weight}\n')
class student(person):
    pass

s=student()
print('Enter information about student\n')
s.acceptPerson()
print('Display information about the student\n')
s.displayPerson()

        
        