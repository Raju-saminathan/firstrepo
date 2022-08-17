class A:
    def feature1(self):
        print('feature 1 is working')

class  B:
    def feature1(self):
        print('feature 2 is working')

class C(A,B):
    def feature(self):
        print('This is the sub class of A and B')  

obj=C()
obj.feature()
obj.feature1()
#MRO - method resolution order will work here (execute from left to right)