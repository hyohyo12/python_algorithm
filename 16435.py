n,l = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
for i in range(0,n):
    if l<h[i]:
        break
    else:
        l+=1
print(l)