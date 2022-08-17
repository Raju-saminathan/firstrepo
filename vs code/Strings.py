 # concatenating strings
a= input('Enter your name \n')
b=('Hi welcome to EMIS ')
print(b+a)

#string slicing program in python
s=input('Enter a string to slice \n')
print(s[:]) 
print(s[0:4]) 
print(s[1:3:2])
print(s[-1:-5:-4]) 

#String functions
word='There are many cat,cow,dogs living here'
print(word.split())
print(word.split(','))
word1='mother:father:brother:sister'
print(word1.split(':'))
print(len(word))
print(word.replace('cat','lion'))
print(word.__contains__('dogs'))
print(word.upper())

def rev(x):
    v=x.split()
    print(v)
    f=v[::-1]  
    print(f)
    f=' '.join(f)
    print(f)


x=input('enter a string\n')
out=rev(x)
