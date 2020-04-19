a=int(input("please enter a positive integer: "))
cubes=[]
i=10
while a>0:
    m=a%i
    a=a//i
    cubes.append(m)
cubes.reverse()
print(cubes)
