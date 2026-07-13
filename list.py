cars= ['Red Bull','Alphine','Haas','Ferrari','Benz']
print(cars)
print(f'Total items in the list {len(cars)}')
print(f'Third item on the list\t{cars[2]}')
print(f'The second item using -ve indexing\t{cars[-2]}')
print(f'Item 2-4\t{cars[1:4]}')
print(f'Return third to last\t{cars[2:]}')
searchvar= input('Enter item to search for\n')
if searchvar in cars:
   print(f'{searchvar}\t exist in your list\n')
else:
 print(f'{searchvar}\t doesnt exist in your list\n')  
teams= ['OKC','BULLS','LAKERS','HEAT','WOLVES','WARRIORS']   
print(teams)
print(f'Total names in the list is {len(teams)}\n')
print(f'The third item in the list is\t{teams[2]}')
print(f'The second item in the list using -ve indexing is\t{teams[-2]}')
print(f'Items 2-5 are\t{teams[1:5]} ')
cars[2]="Cadillac"
cars.remove("Benz")
cars.pop(1)
del cars[3]
cars.clear()
del cars
print(cars)