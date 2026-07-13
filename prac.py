#for x in reversed(range(1,16)):
#   print(x)
   
#print('Happy New Year')
#name='Lewis'
#w#hile name=='Lewis':
#    print
#no=float(input('Enter a number\n'))
#if no%2==0:
#    print(f'{no}\tis an even number')
#else:
#    print(f'{no}\tis an odd number')
#a='babushka'
#b=input('Enter any character\n')
#if b in a:
#    print(f'{b}\tis in a ')
#else:
#    print(f'{b}\tis not in a')
#bPay=float(input('Enter Basic Pay\n'))
#hAllowance=float(input('Enter House Allowance\n'))
#cAllowance=float(input('Enter Commuter Allowance\n'))
#gPay=bPay+hAllowance+cAllowance
#if gPay>0 and gPay<=30000:
#    paye=gPay*0.15
#if gPay>=30001 and gPay<=50000:
#    paye=gPay*0.2
#if gPay>=50001:
#    paye=gPay*0.25
#nPay=gPay-paye
#print(f'basic pay is\t{bPay}\n')
#print(f'house allowance is\t{hAllowance}\n')
#print(f'commuter allowance is\t{cAllowance}\n')
#print(f'gross pay is\t{gPay}\n')
#print(f'net pay is\t{nPay}\n')

#bSalary=float(input('enter basic salary:\n'))
#oHours=float(input('Enter overtime hours \n'))
#if oHours<=50:
#    overtime=oHours*300
#else :
#    overtime=(50*300)+((oHours-50)*350)
#gPay=bSalary+overtime
#if gPay>=1 and gPay<=30000:
#    paye=0
#elif gPay>=30001 and gPay<=50000:
#    paye=gPay*0.15
#elif gPay>=50001 and gPay<=99999:
#    paye=gPay*0.2
#elif gPay>=100000 and gPay<=150000:
#    paye=gPay*0.25
#elif gPay>150000:
#    paye=gPay*0.3
#else:
#    print('not available')
#nssf=gPay*0.06
#sha=gPay*0.027
#hLevy=gPay*0.015
#nPay=gPay-(paye+nssf+sha+hLevy)
#print(f'your gross pay is\t{gPay}\n')
#print(f'your paye is\t{paye}\n')
#print(f'your net pay is\t{nPay}')
#regno=int(input('Enter registration number\n'))
#name=(input('Enter your name\n'))
#gender=(input('Enter your gender\n'))
#uName=(input('Enter unit name\n'))
#uCode=(input('Enter unit code\n'))
#marks=int(input('Enter  marks\n'))
#while marks<0 or marks>100:
#    print(f'Error!:{marks}\tis invalid')
#    marks=int(input('Enter  marks\n'))
    
#if marks>=70 and marks<=100:
#    grade='A'
#elif marks>=60 and marks<=69:
#    grade='B'
#elif marks>=50 and marks<=59:
#    grade='C'
#elif marks>=40 and marks<=49:
#    grade='D'
#else :
#    marks>=0 and marks<=39
#    grade='F'


    
#print(f'\t\t{regno}\n')
#print(f'\t\t{name}\n')
#print(f'\t\t{gender}\n')
#print(f'\t\t{uName}\n')
#print(f'\t\t{uCode}\n')
#print(f'\t\t{grade}\n')

#pin=input('Enter ATM pin:\n')
#while pin=='1234':
#    print('Access granted')
#    break
#else:
#    print(f'ERROR!:{pin}\tis a wrong pin')
#    pin=input('Enter ATM pin:\n')
#des=input('Enter your destination:\n')
#time=input('Enter time of travel:\n')

#if des=='Voi' and time=='11:00':
#    bus='KBZ 009z'
 #   available=False
   
#elif des=='Kisumu' and time=='9:00':
#    bus='KBX 100x'
#    available=False
    
#elif des=='Mombasa' and time=='8:00':
#    bus='KAQ 998y'
#    available=False

#else:
 #   available=True
  #  print(f'{des}\tavailable\t\t')
#if available==False:
 #   print(f'{bus}\tnot available\t\t')

#lecHall=input('Enter lecture hall:\n')
#timeSlot=input('Enter time slot:\n')
#weekDay=input('Enter day of the week:\n')
#if lecHall=='TH LAB A' and timeSlot=='11:00-2:00' and weekDay=='Tuesday':
#    uName='Database Systems'
#    uCode='CMT 102'
#    lecturer='Joe'
    
#    print(f'{uName}\n{uCode}\n{lecturer}\n')
 #   print('Resource not free')
    
#elif lecHall=='TH LAB A' and timeSlot=='2:00-5:00' and weekDay=='Wednesday':
#    uName='Operating Systems'
#    uCode='CMT 103'
#    lecturer='Phil'
    
 #   print(f'{uName}\n{uCode}\n{lecturer}\n')
  #  print('Resource not free')
#elif lecHall=='TH LAB B' and timeSlot=='11:00-2:00' and weekDay=='Friday':
#    uName='Logic Programming'
#    uCode='CMT 104'
#    lecturer='Christiana'
    
 #   print(f'{uName}\n{uCode}\n{lecturer}\n')
  #  print('Resource not free')
#else:
#    print('Resource is free')

#j=2
#while  j<100:
#    print(j)
#    j+=2
#num=2
#while num<100:
#  if num %2==0:
#    print(num)    
#  num+=1  
#sum = 0.0
#avg = 0.0
#odd = 3.0
#count = 0.0

#while odd < 102:
#    sum += odd  # Add the current odd number FIRST
#    count += 1
#    odd += 2    # Then increment to the next odd number

#avg = sum / count

#print(f"Sum: {sum}")
##print(f"Count: {count}")
#print(f"Average: {avg}")
#sum = 0.0
#count = 0.0
#for even in range(2,100,2):
#  sum+=even
#  count+=1
  
#avg=sum/count
#print(f"Sum: {sum}")
#print(f"Count: {count}")
#print(f"Average: {avg}")
#class user:
#  def __init__(self):
#    self.productName = ""
#    self.productDes = ""
#    self.productCat = ""
#    self.productPrice = 0.0
        
#    self.foundProduct = None
#  def displayMenu(self):
#    
 #   print('\t\tDeals poa catalogue\n')
 #   print('\t\t\t1.Add New Product\n')
  #  print('\t\t\t2.Find Product\n')
  #  print('\t\t\t3.My Cart\n')
  #  print('\t\t\t4.Exit\n')
   # self.userchoice=int(input('Select your choice\n'))
    
    
#  def addProduct(self):
#    self.productName=input('Enter Product Name:\n')
#    self.productDes=input('Enter Product Description:\n')
#    self.productCat=input('Enter Product Category:\n')
#    self.productPrice=input('Enter Product Price:\n')
#  def findProducts(self):
#    self.category=input('Enter Category:\n')
#    self.minPrize=input('Enter Minimum Prize:\n')
#    self.maxPrize=input('Enter Maximum Prize:\n')
#  def myCart(self):
#    print('Product name\t\tDescription\t\tCategory\t\tPrice')
#    print(f'{self.productName}\t\t{self.productDes}\t\t{self.productCat}\t\t{self.productPrice}')
#  def exitMenu(self):
#    exit


#j=2
#while j<100:
#  print(j)
#  j+=2
#j=0
#while j<100 :
#  if j%2==0:
#    if j>0:
#     print(j)
#  j+=1
#j=3
#count=0
#add=0
#while j<102: 
#  add+=j
#  count+=1
#  print(j)
#  j+=2
#  avg=add/count
#print(count)
#print(add)
#print(avg)
#even=0
#count=0
#total=0
#for even in range(2,100,2):
#  count+=1
#  total+=even
#  avg=total/count
#  print(even)
#print(count)
#print(total)
#print(avg)
#name=input('Enter employee name\n')
#gender=input('Enter employees gender\n')
#jobGrade=input('Enter employee job grade\n')
#if jobGrade=='H':
#  bSalary=12000
#  hAllowance=2000
#  cAllowance=3000
#  print('bSalary,hAllowance,cAllowance')
#elif jobGrade=='M':
#  bSalary=12000
#  hAllowance=0
#  cAllowance=0
#  print(f'{bSalary},{hAllowance},{cAllowance}')
#elif jobGrade=='S':
#  bSalary=60000
#  hAllowance=40000
#  cAllowance=12000
#  print(f'{bSalary},{hAllowance},{cAllowance}')
#else:
#  print('N/A')

#class movie:
# def __init__(self):
#  print('*'*50)
#  print('\t\tMovie Search\n')
#  print('\t\t1.New Movie\n')
#  print('\t\t2.Find Movie\n')
#  print('\t\t3.Display Movies\n')
#  print('\t\tExit\n')
#  print('*'*50)
#  
  
# def AddMovie(self):
   
##   self.mName=''
#   self.mType=''
#   self.mRelease=''
#   self.mRating=''
#   self.yRelease=''
#   self.actor=''
#   self.price=''
   
# def FindMovie(self):
#  self.mName=input('Enter movie name:\n')
#  self.mType=input('Enter movie type:\n')
#  self.mRating=input('Enter movie rating:\n')
#  self.yRelease=input('Enter year of release:\n')
# def DisplayMovies(self):
#   print('\tMovie name\tGenre\tRating\tRelease Year\tActor\tPrice\n')
#   print(f'\t{self.mName}\t{self.mType}\t{self.mRating}\t{self.yRelease}\t{self.actor}\t{self.price}\n')
# def ExitMenu(self):
#   exit()
   
#m=movie()
#choice=int(input('Enter user choice:\n'))
#if choice==1:
#  m.AddMovie()
#elif choice==2:
#  m.FindMovie()
#elif choice==3:
#  m.DisplayMovies()
#elif choice==4:
#  m.ExitMenu()
class buy:
  def __init__(self):
    self.pName=''
    self.pDes=''
    self.pCategory=''
    self.pPrice=0
    self.pFound=False
  def addProduct(self):
    self.pName = input("Enter product name:\n")
    self.pDes = input("Enter product description:\n")
    self.pCategory = input("Enter product category:\n")
    self.pPrice = int(input("Enter product price:\n "))
    self.pFound = False  
    #product added successfully
  def findProduct(self):
    if self.pName=='':
      print('\n not in the system\n')
      return
    self.sCategory=input('Search for category:\n')
    self.minPrice=int(input('Enter minimum price:\n'))
    self.maxPrice=int(input('Enter maximum price:\n'))
    if self.pCategory==self.sCategory and self.maxPrice>= self.pPrice>=self.minPrice :
       self.pFound=True
       print(f'Product\t{self.pName}\tfound\n')
    else:
      self.pFound=False
      print('No product found\n')
  def myCart(self):
    if self.pFound and self.pName!='':
      print('\tProduct Name\t\tDescription\t\tCategory\t\tPrice\n')
      print(f'\t{self.pName}\t\t\t{self.pDes}\t\t\t{self.pCategory}\t\t\t{self.pPrice}\n')
    else:
      print('Cart empty')
  def exitProgram(self):
    print('Exits program\n')
    return False
b=buy() 
runs=True
while runs:
  print('*'*50)
  print('\t\tDeals Poa Catalogue\n')
  print('\t\t\t1.Add New Product\n')
  print('\t\t\t2.Find Product\n')
  print('\t\t\t3.My Cart\n')
  print('\t\t\t4.Exit\n')
  print('*'*50)
  
  userChoice=int(input('\nSelect user choice\n'))

  if userChoice==1:
    b.addProduct()
  elif userChoice==2:
    b.findProduct()
  elif userChoice==3:
    b.myCart()
  elif userChoice==4:
    runs = b.exitProgram()
  else:
    print('Invalid choice\n')
  if runs:
    input('\nPress enter')

    
    


