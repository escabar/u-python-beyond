class MyClass(object):

    def __init__(self):
        self.i = 1

    def __setitem__(self, value):
        self.i = value

class MyInstance(MyClass):
    def __init__(self, val):
        MyClass.__setitem__(self, val)
        print("in MyInstance init")


#a = MyClass()
#z = MyInstance(5)

#print("MyClass i = ", a.i)
#print("MyClass i = ", z.i)


def my_function(**kwargs):

    print(kwargs)


my_function(first='sol',last='patel')
