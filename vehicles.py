destination=input('Enter destination:\n')
time=input('Enter time of departure:\n')
if destination=='Voi' and time=='11:00':
    regno='KBZ 009z'
    arrivalTime='12:00'
    available=False
elif destination=='Kisumu' and time=='9:00':
    regno='KBX 100x'
    arrivalTime='12:00'
    available=False    
elif destination=='Mombasa' and time=='8:00':
    regno='KAQ 998y'
    arrivalTime='2:00'
    available=False 
else:
    available=True 
if available==False:
    print(f'{destination} not available') 
else:print('Destination available') 
    