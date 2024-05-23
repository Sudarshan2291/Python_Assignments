def cnt():

    x = int(input("enter enter the list length:"))
    list1 = []

    for i in range(x):
    
        inp = int(input("enter the list element:"))
        list1.append(inp)


    z = int(input("enter the element which count you want!:"))
    return list1.count(z)

result=cnt()
print(result)




