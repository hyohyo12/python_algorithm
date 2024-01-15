n = int(input())
score = []
temp = 0
ans = 0
gap = 0
for i in range(n):
    score.append(int(input()))
temp = score[n-1]
for i in range(n-2,-1,-1):
    if temp <= score[i]:
        gap = score[i] - temp + 1
        ans += gap
        temp = score[i] - gap
    else:
        temp = score[i]
print(ans)