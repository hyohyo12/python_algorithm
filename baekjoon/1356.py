n = int(input())
n = list(map(int,str(n)))
front = 1
back = 1
if len(n) == 1:
    print("NO")
else:
    for i in range(0,len(n)):
        front *= n[i]
        for j in range(i+1,len(n)):
            back *= n[j]
        if front == back:
            print("YES")
            break
        else:
            back = 1
    else:
        print("NO")