def dfs(nums,n,m,tmp_stack,idx):
    if len(tmp_stack) == m:
        print(" ".join(map(str,tmp_stack)))
        return
    pre = 0
    for i in range(idx,n):
        if pre != nums[i]:
            tmp_stack.append(nums[i])
            pre = nums[i]
            dfs(nums,n,m,tmp_stack,i)
            tmp_stack.pop()
            
            
            
            
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    s = []
    dfs(nums,n,m,s,0)