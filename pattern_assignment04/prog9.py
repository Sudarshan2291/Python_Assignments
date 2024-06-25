
row = int(input("enter the number of rows:"))

for i in range(row):
    for j in range(row):
        print(j+1,chr(68-j),sep='',end=" ")

    print()




