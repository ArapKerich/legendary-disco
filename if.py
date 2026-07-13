bPay=float(input('Enter basic pay\n'))
hAllowance=float(input('Enter hAllowance\n'))
cAllowance=float(input('Enter cAllowance\n'))
#compute grosspay
gPay=bPay+hAllowance+cAllowance
#calculate paye
if gPay>=0 and gPay<=30000:
    paye=0.15*gPay
if gPay>=30001 and gPay<=50000:
    paye=0.2*gPay    
if gPay>=50000:
    paye=0.25*gPay
#get the net pay
nPay= gPay-paye
#program output
print(f'Basic pay\t{bPay}\n')
print(f'House Allowance\t{hAllowance}\n')
print(f'Commuter Allowance\t{cAllowance}\n')
print(f'Gross Pay\t{gPay}\n')
print(f'P.A.Y.E\t{paye}\n')
print(f'Net Pay\t{nPay}\n')