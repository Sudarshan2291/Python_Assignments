
row = int(input("enter the number of rows:"))

n = 0
for i in range(row):
    for j in range(row):
        print(chr(n+65),end=" ")
        n+=1
    n-=1
    print()

