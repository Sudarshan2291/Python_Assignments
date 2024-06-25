
row = int(input("enter the number of rows:"))

for i in range(row):
    for j in range(row):

        if i%2==0:
            if j%2==0:
                print("$",end=" ")
            else:
                print("=",end=" ")

        else:
            if j%2==0:
                print("=",end=" ")
            else:
                print("$",end=" ")
    print()
    



