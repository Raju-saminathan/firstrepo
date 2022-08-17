x=input("enter ur name : ")
z=""  # empty string
l=[]
a=0
for i in x:

    if(i!=" "):
        z+=i
        a += 1
    if(i==" "):
        l.append(z)
        #print(z)
        z=""
        a += 1
    if(a==len(x)):
        l.append(z)
        #print(z)
        break;

l.reverse()
print(l)
for i in l:
    if i=="  ":
        continue
    else:
        print(i,end=" ")



