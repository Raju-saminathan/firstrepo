My_list=[2,4,6,7,8,9]
sumOfSquare=0
for i in My_list:
    sumOfSquare+=i*i

print(sumOfSquare)

'''another method/using sum function'''

print(sum(i*i for i in My_list))