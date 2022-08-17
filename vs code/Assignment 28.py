'''Iterate Set Items'''
my_set={80,23,24,25,45,26,32,24}
for i in my_set:
    print(i)

'''Find smallest item in the set'''
num={5,8,7,6,4,3}
 #print(min(num))
E_set=set()
number=int(input('enter the total set items: '))
for i in range(number):
     val=int(input("enter the value"))
     E_set.add(val)

print(E_set)
sortSet=sorted(E_set)
print("The smallest value is "+str(sortSet[0]))

'''methods used in list,set,tuple,dictionary'''
l=[20,34,5,66,78,42,5]
print(l.append(60),l)
print(l.index(5))
print(l.count(5))
print(l.pop())
print(l.sort(),l)

s={22,54,66,12,34,77}
s.add(15)
print(s)
s.remove(66)
print(s)
s.pop()
print(s)
print(s.copy())
s.clear()
print(s)

t=(8,3,4,6,7,4,9)
print(len(t))
print(min(t),max(t))
print(t.index(8))
print(sorted(t))
print(sum(t))

animals={'a':'Tiger','b':'Lion','c':'Cat'}
print(animals['a'])
print(len(animals))
print(*animals.keys())
print(*animals.values())
animals['d']='dog'
print(animals)
print(animals.get('d'))

'''List to string'''
def Convert(l):
    strng=''
    for j in range(len(l)):
        if j==len(l)-1:
          strng=strng+l[j]
        else:
            strng=strng+l[j]+","
                        
    strng="'"+strng+"'"
    
    return strng
        
l=[]
n=int(input("enter the number of elements in a list :"))
for i in range(0,n):
    l.append(input())

print(l)
print(Convert(l))



