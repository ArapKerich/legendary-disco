#list=['car','house','jail','rubberduck']
#print(list)
#print(f'{len(list)}')
#list.append('baby')
#list.append(1)
#list.insert(2,'three')#certain position
#list.extend([4,5,6])#add from another list
#list.remove('car')
#list.pop(0)
#del list[0]
#list=['car','cow','can']
#vehicle,animal,verb=list

#print(vehicle,animal,verb)
#tList=[0,1,2,3,4,5,6,7,8,9]
#print(tList[::2])#prints after intervals of 2
#print(tList[::3])
#print(tList[::4])
#print(tList[::5])
#print(tList[::6])
#print(tList[::-1])
#print(tList[::-2])
#print(tList[::-3])
#print(tList[::-4])
#print(tList[4:9:1])
#tList=tList+[10,11,12,13,14,15]#concatenation
#tList[0]='a'
#tList[1]='b'
#tList[2]='c'
#tList[3]='d'
#tList[4]='e'
#tList[5:]='f','g','h','i','j'
#tList.remove('a')
#tList.remove('b')
#tList.remove('c')
#tList.remove('d')
#tList.pop(0)
#del tList[1]
#tList.clear()
#tList.extend([0,1,2,3,4,5,6,7,8,9])
#print(tList.index(4))  #prints what is at index 4
#tList.sort()
#tList.sort(reverse=True) 
#tList.clear()
#tList=[j**2 for j in range(0,10,2)]
#for num in tList:
#    print(num)
#for i in range(len(tList)):
#    print(f"{i}: {tList[i]}")

#print(tList)


#print(list)
#topTen=[]
#for n in range(1,11):
#    topTen.append(n)
#print(topTen)

#myTuple=(1,2,3,4,6)
#aTuple=('bike','truck','jet','scraper','bentley','bmw')
#myTuple=myTuple+aTuple
#oneTuple=(3,)
#print(oneTuple)#tuple with one integer 

#print(myTuple)
#print(myTuple[7:10])
#print(myTuple[7:11])
#print(myTuple[7:])
#print(myTuple[5:8])
#print(myTuple[-3])
#print(myTuple[-3:1])
#repeat=myTuple*2#repeat content in a tuple
#print(repeat)
#print('bike'in myTuple)
#print('bik'in myTuple)
#searchvar=input('Enter item to search for:\n')
#if searchvar in myTuple:
#    print('true')
#else:
#    print('false')
#count=myTuple.count('bmw')
#print(count)
#index=myTuple.index('bmw')
#print(index)
#for truck in myTuple:
#    print(truck)
#for num in myTuple:
#    print('5')
#for index,jet in enumerate(myTuple):
#    print(index,jet)
#student=('grade 11','male','6 foot')
#grade,gender,height=student

#print(grade,gender,height)
#mylist=list(student)
#mylist.append('arthur house')
#student=tuple(mylist)
#print(student)
#sMarks=(
#    ('james','45','D'),
#    ('jane','65','B'),
#    ('jay','85','A')
#    )
#for name, marks, grade in sMarks:
#    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
#print(sMarks)
# ============================================================
# DEALS POA CATALOGUE SYSTEM
# Modular Programming Example
# CMT 210 - Object Oriented Programming I
# ============================================================



class Buy:
    def __init__(self):
        self.pName = ""
        self.pDes = ""
        self.pCategory = ""
        self.pPrice = 0.0
        self.found = False
    
    def addProduct(self):
        print("\n--- ADD NEW PRODUCT ---")
        self.pName = input("Enter product name: ")
        self.pDes = input("Enter product description: ")
        self.pCategory = input("Enter product category: ")
        self.pPrice = float(input("Enter product price: Kshs "))
        self.found = False
        print("\n✓ Product '" + self.pName + "' added successfully!")
        print("-" * 40)
    
    def findProduct(self):
        print("\n--- FIND PRODUCT ---")
        if self.pName == "":
            print("\n✗ No product in the system. Please add a product first.")
            print("-" * 40)
            return
        search_category = input("Enter search category: ")
        min_price = float(input("Enter minimum price: Kshs "))
        max_price = float(input("Enter maximum price: Kshs "))
        if (self.pCategory == search_category and min_price <= self.pPrice <= max_price):
            self.found = True
            print("\n✓ Product found matching your criteria!")
            print("  Name: " + self.pName)
            print("  Category: " + self.pCategory)
            print("  Price: Kshs " + str(self.pPrice))
        else:
            self.found = False
            print("\n✗ No product found matching your search criteria.")
        print("-" * 40)
    
    def myCart(self):
        print("\n--- MY CART ---")
        if self.found and self.pName != "":
            print("=" * 80)
            print("Product Name         Description               Category        Price")
            print("=" * 80)
            print(self.pName + "                 " + self.pDes + "                " + self.pCategory + "        Kshs " + str(self.pPrice))
            print("=" * 80)
            print("Total: Kshs " + str(self.pPrice))
        else:
            print("\nYour cart is empty.")
            print("Please add a product and find it first before viewing the cart.")
        print("-" * 40)
    
    def exitProgram(self):
        print("\nThank you for using Deals Poa Catalogue!")
        print("Exiting program...")
        return False

# ============== PROGRAM STARTS HERE ==============
b = Buy()
running = True

while running:
    print("*" * 50)
    print("\t\tDeals Poa Catalogue")
    print("*" * 50)
    print("\t\t1. Add New Product")
    print("\t\t2. Find Product")
    print("\t\t3. My Cart")
    print("\t\t4. Exit")
    print("*" * 50)
    
    userChoice = input("\nEnter your choice (1-4): ")
    
    if userChoice == "1":
        b.addProduct()
    elif userChoice == "2":
        b.findProduct()
    elif userChoice == "3":
        b.myCart()
    elif userChoice == "4":
        running = b.exitProgram()
    else:
        print("\n✗ Invalid choice! Please enter 1, 2, 3, or 4.")
    
    if running:
        input("\nPress Enter to continue...")