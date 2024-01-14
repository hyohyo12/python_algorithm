n,k = map(int,input().split())
divisor=[]
tmp=1
for i in range(1,n+1):
    if(n%i==0):
        divisor.append(i)
try:
    print(divisor[k-1])
except:
    print(0)