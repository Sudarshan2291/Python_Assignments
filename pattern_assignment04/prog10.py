
row = int(input("enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if j%2==0:
            print(chr(65+j),end=" ")
        else:
            print(row*i+j+1,end=" ")

    print()






