class person:
    def __init__(self):
        pass 
    def getPerson(self):
        self.name=input('Enter your name:\n')
        self.natId=input('Enter your national ID number:\n')
        self.dob=input('Enter your date of birth:\n')
class student(person):
    def __init__(self):
        pass
    def getStudent(self):
        super().getPerson()
        self.regNo=int(input('Enter your registration number:\n'))
        self.course=input('Enter your course of study:\n')
        self.yearStudy=input('Enter your year of study:\n')
    def displayStudent(self):
        print('*'*100)
        print('Student name\tNational ID\tDate of birth\tRegistration number\tCourse\tYear of study\n')
        print(f'{self.name}\t\t{self.natId}\t\t{self.dob}\t\t{self.regNo}\t\t\t{self.course}\t\t{self.yearStudy}\n')
        print('*'*100)
class lecturer(person):
    def __init__(self):
        pass
    def getLecturer(self):
        super().getPerson()
        self.employeeNo=int(input('Enter your employee number:\n'))
        self.department=input('Enter your department:\n')
        self.mSalary=int(input('Enter your monthly salary:\n'))
    def displayLecturer(self):
        print('*'*100)
        print('Lecturer name\tNational ID\tDate of birth\tEmployee number\tDepartment\tMonthly Salary\n')
        print(f'{self.name}\t\t{self.natId}\t\t{self.dob}\t\t{self.employeeNo}\t\t{self.department}\t\t{self.mSalary}\n')
        print('*'*100)
s=student()
s.getStudent()
s.displayStudent()
l=lecturer()
l.getLecturer()
l.displayLecturer()