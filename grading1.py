def studentGrade(marks):
    if marks>=70 and marks<=100:
        grade='A'
    if marks>=60 and marks<=69:
        grade='B'
    if marks>=50 and marks<=59:
        grade='C'
    if marks>=40 and marks<=49:
        grade='D'   
    if marks>=0 and marks<=39:
        grade='F'
    return grade
#read students marks
marks=float(input('Enter student marks\n'))
print(f'Marks:\t{marks}\tGrade:\t{studentGrade(marks)}')