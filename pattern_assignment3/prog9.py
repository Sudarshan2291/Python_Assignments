
row = int(input("enter the number of rows:"))

for i in range(row):
    for j in range(i+1):
        print(chr(69-j),end=" ")
    print()



