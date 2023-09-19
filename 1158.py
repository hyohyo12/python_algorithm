n,k = map(int,input().split())
nums = list(i for i in range(1,n+1))
tmp = 0
ans = []
while len(nums)!=0:
    tmp += (k-1)
    if tmp >= len(nums):
        tmp = tmp%len(nums)
    ans.append(str(nums.pop(tmp)))
print('<',', '.join(ans)[:],'>',sep="")