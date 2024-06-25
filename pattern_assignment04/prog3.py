
row = int(input("enter the number of rows:"))

for i in range(row):
    if i%2==0:
        n=2
        for j in range(row):
            print(n,end=" ")
            n+=2
    else:
        n=1
        for j in range(row):
            print(n,end=" ")
            n+=2

    print()


