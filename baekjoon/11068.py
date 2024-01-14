import sys
input = sys.stdin.readline
def find_palindrome(n:int)->int:
    for i in range(2,65):
        nums = []
        tmp = n
        while tmp > 0:
            nums.append(str(tmp%i))
            tmp //= i
        # if list(nums) == list(nums)[::-1]:
        #     return 1
        if is_palindrome(list(nums)):
            return 1
    else:
        return 0
def is_palindrome(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] != nums[right]:
            return False
        left+=1
        right-=1
    return True
if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        print(find_palindrome(n))