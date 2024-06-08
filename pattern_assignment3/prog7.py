
row = int(input("enter the number of rows:"))
n= 1
for i in range(row):
    for j in range(i+1):
        print(n,end=" ")
        n+=1
    n-=1
    print()




