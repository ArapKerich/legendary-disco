#sum=0.0
#avg=0.0
#odd=0
#j=2
#while j<=102:
#    if j%2==1:
#        sum+=j
#        odd+=1
#    j+=1
#else:
#    avg=sum/odd
#    print(f'Total no of odd numbers\t{odd}')
#    print(f'Sum of odd numbers\t{sum}')  
#    print(f'Average  of odd numbers\t{avg}')
j=0          
while j<=102:
    if j%2==1:
        sum+=j
        odd+=1
    j+=1
else:
    avg=sum/odd
    print(f'Total no of odd numbers\t{odd}')
    print(f'Sum of odd numbers\t{sum}')  
    print(f'Average  of odd numbers\t{avg}')