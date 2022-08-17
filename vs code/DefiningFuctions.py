from array import *
l=array('i',[])
z=len(l)
top=-1
def In(val):
    if top >=z:           
        print('It is full')
    else:
        top+=1
        l[top]=val

def out():
    if top<=-1:
        print('There is nothing in the stack')
    else:
        print('The popped element is',l[top])
        top-=1


In(0)

