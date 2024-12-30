class A:
    def fun(self, country="india"):
        print("my country is", country)


obj = A()
# defoult arguments
obj.fun("itle")
obj.fun("franc")
obj.fun()
obj.fun("US")