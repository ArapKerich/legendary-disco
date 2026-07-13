class bank:
    def __init__(self):#class constructor
        self.bal=100.0
    def regCustomer(self):
        self.accNo=input('Enter Account No\n')
        self.accName=input('Enter Account Name\n')
        self.branch=input('Enter Branch\n')
    def depCash(self):
        self.depo=float(input('Enter amount to deposit\n'))
        self.bal+=self.depo
    def withdrawalCash(self):
        self.withdraw=float(input('Enter amount to withdraw\n'))
        self.bal-=self.withdraw
    def checkBalance(self):
        print(f'Your bank balance for account\t{self.accNo}:-{self.accName}\t is:\t{self.bal}\n')
#display
userChoice=1
b=bank()
while userChoice==1 or userChoice==2 or userChoice==3 or userChoice==4:
    print(f'\t\t\tBank operations\n')
    print(f'\t\t1.Create Account \n')
    print(f'\t\t2.Deposit Cash\n')
    print(f'\t\t3.Withdraw Cash\n')
    print(f'\t\t4.Check Balance\n')
    print(f'\t\t5.Exit\n')
    userChoice=int(input('Select your choice'))
    
    if userChoice==1:
        b.regCustomer()
    elif userChoice==2:
        b.depCash()
    elif userChoice==3:
        b.withdrawalCash()
    elif userChoice==4:
        b.checkBalance()
    elif userChoice==5:
        exit
    

    
    
        
        
        