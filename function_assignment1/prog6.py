
def parent():
    print("Choice 1.myIndex 2.Mypalindrome")
    x = int(input("Enter your choice:"))

    if (x==1):

        def myind():
            mylst = input("enter the element in the list using comma seperator:").split(',')
            y = input("enter the element that is in list:")
            if y in mylst:
                print("the given element ",y," is in list at ",mylst.index(y)," index")
            else:
                print(y," not in given list")

        myind()


    if (x==2):

        def palindrome():
            wrd = input("enter the element:")
            rev_wrd = wrd[::-1]

            if wrd==rev_wrd:
                print("given word is palindrome")
            else:
                print("given word is not a palindrome")

        palindrome()


parent()





