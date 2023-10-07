n,d = map(int,input().split())
nums = [str(i) for i in range(1,n+1)]
nums = ''.join(nums)
count = 0
d = str(d)
for i in nums:
    if i == d:
        count+=1
print(count)