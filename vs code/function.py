from array import *

class User(object):
    l=array('i',[])
    z=len(l)
    top=-1
    def __init__(self,n):
        self.l=[None]*n
        self.z=n
    def In(self,n):
        if self.top<=self.z:
            self.top+=1
            self.l[self.top]=n
        else:
            print('elements are full')
        print(self.l)
       
u=User(5)
u.In(1)
u.In(3)


