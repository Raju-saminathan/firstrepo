class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        return self.m1+other.m1,self.m2+other.m2


s1=Student(30,20)
s2=Student(30,30)
s3=s1+s2
print(s3)

