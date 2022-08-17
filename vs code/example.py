
class Dog:
    def __init__(self,name,legs,color):
        self.name=name
        self.legs=legs
        self.color=color
    def speak(self):
        print("The name of the dog is "+self.name )
        print("The dog has "+str(self.legs)+ ' legs')
        print("The color of the dog is "+self.color )

my_dog=Dog('tiger',4,'black')
my_dog.speak()
dog2=Dog('daisy',6,'grey')
dog2.speak()

        
