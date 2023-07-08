n=int(input())
m=int(input())
arr=[]
count=0
for i in range(n,m+1):
    for j in range(1,i):
        if(i%j==0):
            count+=1
    if(count==1):
        arr.append(i)
    count=0
if(len(arr)==0):
    print(-1)
else:
    print(sum(arr))
    print(min(arr))