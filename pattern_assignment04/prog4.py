
row = int(input("enter the number of rows:"))
n = 1
for i in range(row):
    m = 2+i
    for j in range(row):
        print(n,end=" ")
        n+=m
    n = n-m
    print()



