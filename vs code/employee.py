class Employee(object):

    def __init__(self,empId,empName,city):
        self.empId=empId
        self.empName=empName
        self.city=city
    def __repr__(self):
       return str((self.empId, self.empName,self.city))
    def getDetail(self):
        print(self.empId,self.empName,self.city)

a=Employee(617,'sami','chennai')
b=Employee(600,'raju','banglore')
c=Employee(612,'rajubai','banglore')
empList=[a,b,c]
a.getDetail()
b.getDetail()

print(*sorted(empList,key=lambda x: x.empId),sep='\n')  


    



        