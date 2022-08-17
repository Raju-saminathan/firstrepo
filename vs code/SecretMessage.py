import math

s='hello world'
s1=s.replace(' ','')
length=len(s1)  
column=math.ceil(math.sqrt(length))

code=''
for i in range(0,column):
    for j in range(i,length,column):
        code+=s1[j]

    code+='\n'
    
print(code)

