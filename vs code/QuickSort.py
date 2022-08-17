def partition(l,r,num):
    pivot,pointer=num[r],l           #pivot is last and pointer is first
    for i in range(l,r):
        if num[i]<=pivot:            #swapping values smaller than pivot
            num[i],num[pointer]=num[pointer],num[i]
            pointer+=1   
    num[pointer],num[r]=num[r],num[pointer] 
    return pointer

def sort(l,r,num):   
    if len(num)==1:
        return num
    if l<r:
        pi=partition(l,r,num)
        sort(l,pi-1,num)
        sort(pi+1,r,num)
        return num

arr = [4,6,9,3,2,5] 
print(sort(0,len(arr)-1,arr))
