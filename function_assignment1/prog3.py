arr = []
x = int(input("enter the length"))
for i in range(1,x+1):
    y=int(input("enter the element"))
    arr.append(y)
    

def fact(arr_x):
    for i in range(len(arr_x)):
        a=1
        z=arr_x[i]
        for j in range (1,z+1):
            a=a*j
        arr_x[i]=a
    return arr_x

x=fact(arr)
print(x)



