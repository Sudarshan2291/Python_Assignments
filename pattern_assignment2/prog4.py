n = int(input("enter the number of rows"))
cn = 2
l = 3
for i in range(n):

    for j in range(n):

        print(cn,end=" ")
        cn = cn + l
        l += 2
    print()


