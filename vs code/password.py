class Validation(object):

    def __init__(self,n):
        self.n=n
    def lower(self):
        lower= any(c.islower() for c in self.n)
        return lower
    def upper(self):
        upper=any(c.isupper() for c in self.n)
        return upper
    def digit(self):
        digit=any(c.isdigit() for c in self.n)
        return digit

    def validate(self):
        lower=self.lower()
        upper=self.upper()
        digit=self.digit()

        length=len(self.n)
        Weak=lower
        medium= (upper and lower)
        strong= (lower and upper and digit and length>=6)
         
        if strong:
            print('YOUR PASSWORD STRENGTH IS STRONG')
            return 'YOUR PASSWORD SUCCESSFULLY GENERATED'
            return True
        elif medium:
            print('YOUR PASSWORD IS NOT STRONG ADD INTEGERS IN YOUR PASSWORD')
            return False
        elif Weak:
            print('YOUR PASSWORD IS VERY WEAK')
            return False;          
        
def call():
    c=input("PLEASE SET A STRONG PASSWORD: ")
    B=Validation(c)
    while(not B.validate()):
        c=input("PLEASE SET A STRONG PASSWORD: ")
        B=Validation(c)
         

call()



