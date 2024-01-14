import sys
input = sys.stdin.readline
def my_round(n):
    if n-int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)


nums = []
n = int(input())
if n:
    for i in range(n):
        nums.append(int(input()))

    nums.sort()
    nn = my_round(n*0.15)
    if nn > 0:
        print(my_round(sum(nums[nn:-nn])/len(nums[nn:-nn])))
    else:
        print(my_round(sum(nums)/len(nums)))
else:
    print(0)