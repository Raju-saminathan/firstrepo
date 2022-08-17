A=int(input('Enter the first number '))
B=int(input('Enter the second number '))
C=int(input('Enter the third number '))
D=A,B,C
for i in D:
    if A>B and A>C:
        print('The largest number is '+str(A))
        break
    elif B>C and B>A:
        print('The largest number is '+str(B))
        break
    else:
        print('The largest number is '+str(C))
        break