class test :
    def __init__(self):
        self.a="old"
        self.b(self.a) # obj.b(old)
    def b(self,c):
        print("dfghj")
        self.c = "new"
obj = test()
print(obj.a)
print(obj.__dict__)
# print(obj.b("old"))
