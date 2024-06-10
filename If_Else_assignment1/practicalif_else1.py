



#1)

x= int(input())
y= int (input())

if (x>y):
    print(x,'is max number between',x,'&',y)
else:
    print(y,'is max number between',x,'&',y)
'''
o/p:
1
2
2 is max number between 1 & 2
'''



#2)

x= int(input())

if x>0:
    print(x,'is positive number')
elif x<0:
    print(x,'is negative number')
else:
    print(x,'is zero')
'''
o/p:
-2
-2 is negative number
'''



#3)

x= int(input())

if x%2==0:
    print(x,'is an Even number!')

else:
    print(x,'is an Odd number!')

'''    
o/p:
4
4 is an Even number!
'''


#4)


x= int(input())

if (x%5==0): 
    print(x,'is divisible by 5')

else:
    print(x, 'is not divisible by 5')
'''
o/p:
55
55 is divisible by 5

'''




#5)

x= int(input("enter the value from 0 to 6: "))

if (x==0):
    print("Monday")

elif (x==1):
    print("Tuesday")

elif (x==2):
    print("Wednesday")

elif (x==3):
    print("Thursday")

elif (x==4):
    print("Friday")

elif (x==5):
    print("Saturday")

elif (x==6):
    print("Sunday")
        
else:
    print("enter the value between 0to6")

'''
o/p:
enter the value from 0 to 6: 5
Saturday
'''



#6)


x= input('Enter the character:')
y= x.isalpha()
if (y):
    print(x,'is aplhabet')

else:
    print(x,'is not a aplhabet')

'''
o/p:
Enter the character:v
v is aplhabet
'''



#7)

x= int(input())

if (x==1):
    print('January is a 31-day month.')
elif (x==2):
    print('February is a 28/29-day month.')
elif (x==3):
    print('March is a 31-day month.')
elif (x==4):
    print('April is a 30-day month.')
elif (x==5):
    print('May is a 31-day month.')
elif (x==6):
    print('June is a 30-day month.')
elif (x==7):
    print('July is a 30-day month.')
elif (x==8):
    print('August is a 31-day month.')
elif (x==9):
    print('September is a 30-day month.')
elif (x==10):
    print('Octomber is a 31-day month.')
elif (x==11):
    print('November is a 30-day month.')
elif (x==12):
    print('December is a 31-day month.')
else:
    print('enter the number between 1 to 12')

'''
o/p:
4
April is a 30-day month.

'''




#8)

x= int(input())

if (x>10):
    print('yes',x,'is greater than 10')

elif (x<10):
    print("no",x,"is less than 10")

else:
    print(x,"is equal to 10")

'''
o/p:
12
yes 12 is greater than 10
 
2
no 2 is less than 10
'''



#9)

x= input("enter the character:")

if (x=='a' or x=='e'or x=='o' or x=='u' or x=='i'):
    print("vowel")

else:
    print("consonant")

'''
o/p:
enter the character:a
vowel
 
enter the character:b
consonant
'''



#10)
x= int(input("enter the year:"))

if (x%4==0 and x%100!=0)or (x%400==0):
    print(x,"is the year is leap year")

else:
    print(x,"is not a leap year")

