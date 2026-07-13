class person:
    def __init__(self):
         self.name=input('Enter Name:\n')
         self.gender=input('Enter Gender:\n')
         self.dob=input('Enter date of birth:\n')
class staff(person):
    def __init__(self):
        self.staffNo=input('Enter staff no:\n')
        self.dept=input('Enter department name:\n')
        super().__init__()
        self.displayStaff()#calls def init to enter name gender and dob
    def displayStaff(self):
       print(f'Staff No\t{self.staffNo}\n')
       print(f'Department\t{self.dept}\n')
       print(f'Staff Name\t{self.name}\n')
       print(f'Staff Gender\t{self.gender}\n')
       print(f'Date of birth\t{self.dob}\n')
sta=staff()
    