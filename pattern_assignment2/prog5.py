k = int(input("enter the number:"))
n = 1

for i in range(k):

    for j in range(k):

        if j%2==0:
            print(n**2,end=" ")
            n = n+1
        else:
            print(n,end=" ")
            n = n+1

    print()





