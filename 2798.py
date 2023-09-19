import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))
temp = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cards = num[i]+num[j]+num[k]
            if cards > m:
                continue
            else:
                temp.append(cards)
print(max(temp))