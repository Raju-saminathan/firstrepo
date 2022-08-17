# def swap(x):
    
#     s=""
#     l=[]
#     count=0
#     for i in x:
#         if (i!=" "):
#             s+=x
#             count+=1
#         if (i==" "):
#             l.append(s)
#             count+=1
#             s=""
#         if (count==len(x)):
#             l.append(s)
#             break
    
#     print(l)

# x=input('Enter a string\n')
# swap(x)



# class User(object):
#     s=''
#     l=[]
#     count=0
#     def rev(self,x):
#         for i in self.x: 
#             if (i!=" "):
#                   self.s+=self.x
#                   self.count+=1
#             if (i==" "):
#                   self.l.append(s)
#                   self.count+=1
#                   self.s=''
               
#             if (self.count==len(self.x)):
#                  self.l.append(self.s)
#                  break

# x=input('Enter something\n')
# u=User()
# u.rev(x)

# x=input("Enter a string to reverse")
# z=""  # empty string
# l=[]
# count=0
# for i in x:

#     if(i!=" "):
#         z+=i
#         count += 1
#     if(i==" "):
#         l.append(z)
#         z=""
#         count += 1
#     if(count==len(x)):
#         l.append(z)
#         break;

# print(l)

# str=input('enter a string')
# v=str[::-1]
# print(v)

# tup=input('enter a randome numbers')
# print('hello')
# print(type(tup))

for i in range(0,column):
    for j in range(i,length,column):
        code+=s1[j]

    code+='\n'
    

print(code)