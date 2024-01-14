import sys
input = sys.stdin.readline
def get_tip(n,nums):
    nums.sort(reverse=True)
    tip = 0
    for i in range(n):
        tmp = nums[i]-((i+1)-1)
        if tmp <= 0:
            break
        tip+=tmp
    return tip
    
if __name__=="__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(get_tip(n,nums))