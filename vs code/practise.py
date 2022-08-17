stack=[]
l=len(stack)
top=-1
def In(val):
    if top>l-1:
        print('full')
    else:
        top+=1
        l[top]=val
In(0)
print(stack)



