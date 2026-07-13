#program to initialize a value with a string value programming. The program will prompt the user to enter a character from keyboard then confirm if that character is present in the string
value= 'Programming'
char= input('Enter Character to search')
if char in value:
    print(f'{char}\t is present in {value}')
else:
    print(f'{char}\t is not present in {value}')