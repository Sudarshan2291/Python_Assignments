n = int(input("enter the number of rows:"))

for i in range(n):
    for j in range(n):
        print(chr(64+n-j),end="")
        print(n-j,end=" ")
    print()

