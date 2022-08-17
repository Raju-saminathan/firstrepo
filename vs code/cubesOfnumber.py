def printCubes(a,b):
    for i in range(a,b+1):
        j=1
        for j in range(j**3,i+1):
            if(j**3==i):
                print(j**3,end=' ')
                break

a=1;b=300
print('cubes of the given range is: ')
printCubes(a,b)
