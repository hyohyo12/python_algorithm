import sys
input = sys.stdin.readline
n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
w.sort(reverse=True)
res = []
for j in range(n):
   res.append((j+1)*w[j])
print(max(res))