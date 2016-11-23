class MyClass(object):
    """docstring for MyClass."""
    def __init__(self):    # Constractor
        super(MyClass, self).__init__()
        self.name = ""

    def getName(self):
        return self.name

    def setName(self, _name):
        self.name = _name

a = MyClass()
a.setName("NAME")
print(a.getName())
