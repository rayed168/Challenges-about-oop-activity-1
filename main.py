class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a < other.a:
            return "Object 1 is less than object 2"
        else:
            return "Object 2 is less than object 1"
    def __eq__(self,other):
        if self.a == other.a:
            return "Object 1 is equal to object 2"
        else:
            return "Object 1 is not equal to object 2"
obj1=A(3)
obj2=A(5)
print(obj1<obj2)
print(obj1==obj2)