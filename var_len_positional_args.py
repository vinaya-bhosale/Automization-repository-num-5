class A:
    def fun(*stu):
        print("student name is", stu[0])
        print("stud roll num is:", stu[1], "student mobil num is", stu[2], " student address is", stu[3])

o = A()
o.fun("vinaya", 21, 1234567891, "pune")