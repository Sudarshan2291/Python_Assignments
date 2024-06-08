
row = int(input("enter the number of rows:"))
n = 1
k = 3
for i in range(row):
    for j in range(i+1):
        print(n,end=" ")
        n=n-1
    print()
    n=n+k+i
    k+=1 




