import array as arr

# take array as an input

arr1=arr.array('i',[])
x = int(input("enter the length of an array"))
for i in range (1,x+1):
    print(i,end=" ")
    y=int(input("element of an array"))
    arr1.append(y)
print(arr1)
# function for a factorial

def fact(arr):
    for i in range(len(arr)):
        a = 1
        z = arr[i]
        for j in range(1,z+1):
            a = a*j
        arr[i]=a
    return arr

print(fact(arr1))


