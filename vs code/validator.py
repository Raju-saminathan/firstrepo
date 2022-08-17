
def validator(pwd):
    digit= any(char.isdigit() for char in pwd)
    lower=any(char.islower() for char in pwd)
    upper=any(char.isupper()for char in pwd)
    length=True if len(pwd)>6 else False
    special_ch=['[','!','@','#','%','$','&','+','-','(',')','/',']']
    splch=any(char in special_ch for char in pwd)
    
    weak=all(length,lower)
    medium=all(length,lower,upper)
    strong=all(length,lower,upper,digit)
    veryStrong=all(length,lower,upper,digit,splch)

    if weak:
        print('your password is weak')
        
        
def call():
    pwd=input("Enter a password")

call()