class Student:
    def calc_avg(self,num):
        sum_num=0
        for t in num:
            sum_num+=t
        avg=sum_num/len(num)
        return avg;

student1=Student()
student2=Student()
print(student1.calc_avg([50,44,66,86,75]))
print(student2.calc_avg([50,65,64,87,65]))

'''printing multiple arguments'''

def mulArg(name,num,bloodGroup):
    print('hi my name is',name)
    print('my mobile number is',num)
    print('my blood group is',bloodGroup)

mulArg('saminathan',7418686317,'o+')