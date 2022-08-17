class Arithmatics:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def operations(self):
        print(f'The addition of {self.num1} and {self.num2} is {self.num1+self.num2}')
        print(f'The substraction of {self.num1} and {self.num2} is {self.num1-self.num2}')
        print(f'The multiplication of {self.num1} and {self.num2} is {self.num1*self.num2}')
        print(f'The division of {self.num1} and {self.num2} is {self.num1/self.num2}')
    
    
perform=Arithmatics(12,5)
perform.operations()    
