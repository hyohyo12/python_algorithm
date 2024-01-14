import sys
N,B=map(int,sys.stdin.readline().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tmp=0
res=''
while N!=0:
    tmp = N%B
    res+=arr[tmp]
    N=N//B 
print(res[::-1])