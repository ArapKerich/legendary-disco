class car:
    def maxSpeed(self):
        print('Maximum speed 260')
class truck:
    def maxSpeed(self):
        print('Maximum speed 80') 
class tractor:
    def maxSpeed(self):
        print('Maximum speed 60')
class bus:
    def speed(self):
        print('Maximum speed 120')
vehicles=[car(),truck(),tractor(),bus()]
for x in vehicles:
    x.maxSpeed()
