
row = int(input("enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if i%2==0:
            print(chr(69-j),end=" ")
        else:
            print(chr(65+j),end=" ")
        
    print()



