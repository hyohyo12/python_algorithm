import sys
input = sys.stdin.readline
def get_low_price(nums):
    tmp = 0
    nums.sort(reverse=True)
    for i in range(2,len(nums),3):
        tmp+=nums[i]
    low_price = sum(nums)-tmp
    return low_price
if __name__ == "__main__":
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    print(get_low_price(price))