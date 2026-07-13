class student:
    def __init__(self,r,n,g,c):
        self.regno=r
        self.name=n
        self.gender=g
        self.course=c
    def display(self):
        print(f'Regno\t:{self.regno}')
        print(f'Name\t:{self.name}')
        print(f'Gender\t:{self.gender}')
        print(f'Course\t:{self.course}')
        
#end of class definition
#read program inputs
regno=input('Enter Registration number\n')
name=input('Enter  name\n')
gender=input('Enter  gender\n')
course=input('Enter course\n')
#instantiate the class

s=student(regno,name,gender,course)#creates an object of type 
#call display function
s.display()
