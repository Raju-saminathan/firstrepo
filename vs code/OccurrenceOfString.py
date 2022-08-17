from collections import Counter
import re

'''iterating a string'''

Str="Demonstrating number of occurrence of a charecter in this string"
char=input('Enter a charecter: ')
count=0
for i in Str:
    if i==char:
        count+=1
print(count)

'''Using counter function'''
c=Counter(Str)
print(c['a'])

'''using regular expression'''

print (len(re.findall('a',Str)))


