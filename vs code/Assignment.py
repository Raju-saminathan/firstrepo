class Computer:
    x="saminathan"            #class variable
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def feature(self):         #instance method
        print(f'feature 1 is {self.f1}')
        print('feature 2 is '+ self.f2)
    @staticmethod               #staticmethod
    def preview():
        print('Hi iam static method')
    
class User1(Computer):
    def __init__(self,a,b):
        self.a=a            #instance variable
        self.b=b  
    def show(self):
        print(self.a)
        print(self.b)
    @classmethod            #class method
    def ss(cls):
        print(cls.x)          #accessing class variable 

class User2(Computer):
    def preview():            #method overriding
        print("static method over ridden")
       

com=Computer('camera','voice')
com.feature()
com.preview()
u =User1('added face recognition','added finger print')   
u.ss()  
u.show()
User2.preview()
