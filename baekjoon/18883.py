n,m = map(int,input().split())
temp = [i for i in range(n*m)]
for i in range(0,len(temp),m-1):
    for