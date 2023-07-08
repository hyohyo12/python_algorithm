TC = int(input())
tmp=[25,10,5,1]
for i in range(TC):
    n = int(input())
    for i in range(4):
        if(i==3):
            print(n//tmp[i])
        else:
            print(n//tmp[i],end=' ')
        n=n%tmp[i]
    n=0