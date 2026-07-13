lecHall=input('Enter Lecture Hall\n')
timeSlot=input('Enter time slot\n')
day=input('Enter day of the week\n')
if lecHall=='TH Lab A' and timeSlot=='11-2' and day=='Tuesday':
    uname='CMT 109-Database Systems'
    lecName='Joe'
    available=False
    
elif lecHall=='TH Lab A' and timeSlot=='2-5' and day=='Wednesday':
    uname='CMT 206-Operating Systems'
    lecName='Phil'
    available=False 
    
elif lecHall=='TH Lab B' and timeSlot=='11-2' and day=='Friday':
    uname='CMT 113-Logic Programming'
    lecName='Christina'
    available=False 
    
else:
    available=True
#program output
if available==False:
    print(f'{lecHall} not avalaible at {day} , {timeSlot}\n')
    print(f'Unit name:{uname}\nLecturer {lecName}\n')
else:
    print('The Hall is free at that time of the day\n')
    

