

row = int(input("enter the number of rows:"))
n = 1
for i in range(row):
    for j in range(row):
        if i%2==0:
            print(n,end=" ")
        else:
            print(n*n,end=" ")
        
        n+=1
    print()



