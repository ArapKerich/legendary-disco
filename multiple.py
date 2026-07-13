class person:
    def getBioData(self):
        self.name=input('Enter name:\n')
        self.gender=input('Enter Gender:\n')
class department:
    def getDepartment(self):
        self.deptName=input('Enter department Name:\n')
class course:
    def getCourse(self):
        self.courseName=input('Enter course name:\n')
class student(person,department,course):
    def __init__(self):
        self.regNo=input('Enter student regno:\n')
        super().getBioData()
        super().getDepartment()
        super().getCourse()
        self.display()
    def display(self):
        print(f'Regno:\t{self.regNo}:\n')
        print(f'Name:\t{self.name}:\n')
        print(f'Gender:\t{self.gender}:\n')
        print(f'Department:\t{self.deptName}:\n')
        print(f'Course:\t{self.courseName}:\n')
stu=student()
        
        
        