sum=0.0
avg=0.0
even=0

for i in range(1,101):
    if i%2==0:
        even+=1
        sum+=i
else:
    avg=sum/even
    print(f'Total even numbers\t{even}\n')  
    print(f'Sum of even numbers\t{sum}\n')  
    print(f'Average  of even numbers\t{avg}\n')  