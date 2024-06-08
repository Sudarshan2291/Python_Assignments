row = int(input("enter the number of rows:"))

for i in range(row):
    for j in range(row-i):
        if j%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()







