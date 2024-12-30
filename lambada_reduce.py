from functools import reduce
lis=(100,200,300)
var=reduce(lambda x,y:x+y,lis )
print(var )