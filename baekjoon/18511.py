from itertools import product

def find_max_num(n,nums):
    length = len(str(n))
    
    while True:
        tmp = list(product(nums,repeat=length))
        candidate = []    
        for i in tmp:
            if int("".join(map(str,i))) <= n:
                candidate.append(int(''.join(map(str,i))))
        if len(candidate)>=1:
            return max(candidate)
        else:
            length-=1
if __name__ == "__main__":
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    print(find_max_num(n,nums))
