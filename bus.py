def busScheduler(time,date,des):
    global regno
    if time=='8' and date=='18/06/2026' and des=='Voi':
        regno='KDW 117K'
        available=True
    elif time=='2' and date=='17/06/2026' and des=='Meru':
        regno='KCA 221W'
        available=True
    else:
        available=False
    return available
#read the 3 parameters
time=input('Enter time of travel\n')
date=input('Enter the date of travel\n')
des=input('Enter your destination\n')
status=busScheduler(time,date,des)#function call
if status==True:
    print(f'Bus registration{regno} is availableat that time\n')
else:
    print('There is no schedule matching the criteria')