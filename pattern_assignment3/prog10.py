
row = int(input("enter the number of rows:"))
n = row
for i in range(row):
    for j in range(row-i):
        print(chr(64+n+j),end=" ")
    print()
    n= n-1




