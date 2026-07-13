countries= ("Kenya","Tanzania","United Kingdom","United States","Kenya")
#print(f"The tuple length is\t{len(countries)}")
#print(f"Third item on the list is\t{countries[2]}")
#print(f"Second last item on the list is\t{countries[-2]}")
#print(countries[1:4])#return item 2 to 4
#print(countries[2:])
#print(countries[:3])
#searchVar= input("Enter item item to search for\n")
#if searchVar in countries:
 #   print(f'{searchVar}\t Exist on the tuple')
#else:
 #   print(f'{searchVar}\t does not exist on the tuple')
#Convert tuple to a list
myList= list(countries)    
#Update the list
myList[4]= "Brazil" 
#convert list to tuple
countries= tuple(myList)
print(countries)
#print(countries)