import sys
input = sys.stdin.readline

n,k = map(int,input().split())
cats = list(map(int,input().split()))
cats = sorted(cats)
count = 0
for i in range(n):
    for j in range(n-1,i,-1):
        if cats[i]+cats[j] <= k:
            count += 1
            cats[j] = k
            break
print(count)