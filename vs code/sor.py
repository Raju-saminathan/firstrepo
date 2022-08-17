

def sortStack(arr,l):
    stack=[]
    i=0
    while i<l:
        stack.append(arr[i])
        i+=1
    tempstack=asscend(stack)
    i=0

arr=[8,5,3,7,2]
l=len(arr)

arr=sortStack(arr,l)