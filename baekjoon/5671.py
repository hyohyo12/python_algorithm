while True:
    try:
        n,m = map(int,input().split())
    except:
        break
    count = 0
    for i in range(n,m+1):
        temp = list(map(int,str(i)))
        if len(temp) == len(set(temp)):
            count+=1
    print(count)