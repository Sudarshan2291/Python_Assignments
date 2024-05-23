
class student:

    total_student = 0       #class variable
    
    def __init__(self,name,marks):      #constructor
        
        self.name=name                  #instance variable
        self.marks=marks                #instance var
        
        student.total_student+=1
    
    def disp_info(self):                #instance method

        print("Name: ",self.name)
        print("Marks: ",self.marks)



name = input("enter the name")
marks = int(input("enter the marks"))
std1 = student(name,marks)
std1.disp_info()

    



