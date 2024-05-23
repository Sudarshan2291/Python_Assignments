
def outer():
    def inner():
        return "Hello,I'm the inner function!"
    return inner
retobj = outer()
retinner = retobj()
print(retinner)


