nums = {}
for i in range(0,10):
    nums[i] = 0
for i in list(map(int,str(int(input()) * int(input()) * int(input())))):
    nums[i] += 1
for j in nums.values():
    print(j)