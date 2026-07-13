class person:
    def __init__(self):
        pass
    def accept(self):
        self.name=input('Enter name\n')
        self.dob=input('Enter date of birth\n')
        self.gender=input('Enter gender\n')
        self.weight=input('Enter weight\n')
        self.height=input('Enter height\n')
    def display(self):
       print(f'{self.name}')
       print(f'{self.dob}')
       print(f'{self.gender}')
       print(f'{self.weight}')
       print(f'{self.height}')

p=person()
p.accept()
p.display()
