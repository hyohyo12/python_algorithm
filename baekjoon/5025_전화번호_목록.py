import sys
input = sys.stdin.readline


def is_prefix(nums:list[str],n:int):
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j][:len(nums[i])]:
                print("NO")
                return
    print("YES")
    return


def main():
    for _ in range(int(input())):
        n = int(input())
        nums = []
        for _ in range(n):
            nums.append(input().strip())
        nums.sort(key=lambda x:len(x))
        is_prefix(nums,n)




if __name__ == "__main__":
    main()