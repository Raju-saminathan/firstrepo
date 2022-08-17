from array import *
'''string slicing program'''
str='Hello There'
print(str[:])
print(str[0:5])
print(str[-5:-1])
print(str[0:10:2])
print(str[1:-1:2])

'''Accessing array elements from array '''
Ar=array('i',[1,2,3,4,5,6])
print(Ar[3])
val=array('u',['p','q','r','s'])
print(val[0],val[2])

'''finding largest element of an array'''
given=array('i',[30,22,23,43,54,10,15])
l=len(given)
max=given[0]
for i in range(1,l):
    if given[i]>max:
        max=given[i]

print(max)

'''Python program to find sum of elements in array'''
num=array('i',[15,2,5,13])
#print(sum(num))
temp=0
for i in num:
    temp+=i

print(temp)

'''Python program to find Cumulative sum of a list'''
my_list=[15,12,13,20,50]
another_list=[]
t=0
for i in range(0,len(my_list)):
    t+=my_list[i]
    another_list.append(t)

print(another_list)

'''Sorting List in Ascending Order'''
list=[7,5,8,4,3,9]
list.sort()
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[j],list[i]=list[i],list[j]
print(list)

'''python program to reverse a tuple'''
t=(-1,-2,-3,-4)
print(type(t))
print(t)
rev=reversed(t)
print(tuple(rev))
