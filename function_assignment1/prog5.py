
# input list from user

x = int(input("enter the length of a list"))
list1 = []
for i in range(x):
    y = int(input("enter the element in the list"))
    list1.append(y)


#Parent function and nested functions
def par(lst1):

    print("choice 1.digit count 2.even Digit Count 3.odd Digit Count")
    inp = int(input("enter your choice: "))

    if (inp==1):
        def digitCnt(lst1):
            return len(lst1)
 
        a=digitCnt(lst1)
        print("the count of elements in list are ",a)

    if (inp==2):
        def Edigitcnt(lst1):
            cnt = 0
            for i in range(x):
                if (lst1[i]%2==0):
                    cnt+=1
            return cnt
        b=Edigitcnt(lst1)
        print("the count of even elements in list are ",b)

    if (inp==3):
        def Odigitcnt(lst1):
            cnt = 0
            for i in range(x):
                if (lst1[i]%2==1):
                    cnt+=1
            return cnt
        c=Odigitcnt(lst1)
        print("the count of odd elements in list are ",c)

par(list1)





