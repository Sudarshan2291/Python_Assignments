
class Sum:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def mySum(self):
        if ((self.x+self.y)%2==0):
            return self.x+self.y ,"Even"
        
        if((self.x+self.y)%2==1):
            return self.x+self.y , "Odd"

a= float(input("enter the 1st number of 1st object:"))
b= float(input("enter the 2nd number:"))
retobj1 = Sum(a,b)
x= retobj1.mySum()
print("sum of two numbers is ",x[0]," and the sum is ",x[1])
 
c= float(input("enter the 1st number of 2nd object:"))
d= float(input("enter the 2nd number:"))
retobj2 = Sum(c,d)
x= retobj2.mySum()
print("sum of two numbers is ",x[0]," and the sum is ",x[1])




