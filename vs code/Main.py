a=[1,2,3,4,5]
def op():
    l=len(a)-1
    x=a[l]
    a.remove(a[l])
    print(x)
op()