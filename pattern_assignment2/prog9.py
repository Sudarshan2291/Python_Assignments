
n = int(input("enter the number of rows:"))
k = 65
for i in range(n):

    for j in range(n):
        if j%2==0:
            print(chr(k),end=" ")
        else:
            print(chr(k+32),end=" ")

        k+=1
    print()








