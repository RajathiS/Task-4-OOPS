class myClass:
    __number= 105
    def __privMeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private value:", self.__number)
private = myClass()
private.hello()

