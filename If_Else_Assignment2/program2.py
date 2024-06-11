






x= int(input("enter the 1st angle:"))
y= int(input("enter the 2nd angle:"))
z= int(input("enter the 3rd angle:"))

if (x+y+z==180):
    
    if(x==90 and y!=90 and z!=90):
        print("It is a right angle triangle")

    elif(x!=90 and y==90 and z!=90):
        print("It is a right angle triangle")

    elif(x!=90 and y!=90 and z==90):
        print("It is a right angle triangle")

    else:
        print("It is not a right angle triangle")


else:
    print("It is not a right angle triangle")

'''
sudarshan@sudarshan:~/python/Assignment/if_else_2$ python3 program2.py
enter the 1st angle:90
enter the 2nd angle:90
enter the 3rd angle:90
It is not a right angle triangle
sudarshan@sudarshan:~/python/Assignment/if_else_2$ python3 program2.py
enter the 1st angle:90
enter the 2nd angle:60
enter the 3rd angle:30
It is a right angle triangle
'''
