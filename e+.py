#!/usr/bin/env python3
print("this f is for calcul 1/x+1/(x+1)+1(x+2)+...+1/(x+n)")
while True:
    n=int(input("n = "))
    x=int(input("x = "))
    if x<=0 or n<x:
        print("NAN!Reinput pls")
        continue
    else:
        sum=0
        for i in range(x,n):
            sum +=1/i
            print("{:2d} {:6.4f}".format(i,sum))
        break
