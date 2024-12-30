class A:
    def fun(self, **stu):
        print("student name", stu['name'])
        print("student roll", stu['roll'], "mob", stu['mob'], "address", stu['addr'])


object = A()
object.fun(name="vinaya", roll=21, mob=1234567898, addr="pune")