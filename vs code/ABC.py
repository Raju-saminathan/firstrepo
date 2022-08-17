from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def act(self):
        return print('This is class A')

class B(A):                   
    def act(self):
        super().act()
        print('This is class B')

class C(B):
    def act(self):
        self.call(self)
    def call():
        print('This is class C')
                          
                              #we cannot create object for abstract class 
b=B()           
b.act()
c=C()
c.act()