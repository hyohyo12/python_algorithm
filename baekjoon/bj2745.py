N,B=input().split()
arr="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N =N[::-1]
count=0
result=0
for i in N:
    result+=arr.index(i)*(int(B)**count)
    count+=1
print(result)