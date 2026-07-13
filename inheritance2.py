class person:
    def __init__(self):
        self.name=input('Enter name\n')
        self.gender=input('Enter Gender\n')
        self.dob=input('Enter date of birth\n')
class staff(person):
   def __init__(self):
       self.staffno=input('Enter staff no\n')
       super().__init__()
       self.display()
   def display(self):
       print(f'Staff No\t{self.staffno}\n')
       print(f'Staff Name\t{self.name}\n')
       print(f'Staff Gender\t{self.gender}\n')
       print(f'Date of birth\t{self.dob}\n')
s=staff()

           
       
           
    