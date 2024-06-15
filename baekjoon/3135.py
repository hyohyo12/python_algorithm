a,b = map(int,input().split())
n = int(input())


seq = [int(input()) for _ in range(n)]
res = abs(a-b)
for num in seq:
    res = min(abs(num-b)+1,res)
print(res)