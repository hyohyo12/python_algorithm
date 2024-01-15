def dfs(visited,nums,n,m,tmp_stack):
    if len(tmp_stack) == m:
        print(" ".join(map(str,tmp_stack)))
        return
    pre = 0
    for i in range(0,n):
        if not visited[i] and pre != nums[i]:
            tmp_stack.append(nums[i])
            pre = nums[i]
            visited[i] = True
            dfs(visited,nums,n,m,tmp_stack)
            visited[i] = False
            tmp_stack.pop()
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    visited = [False] * n
    s = []
    dfs(visited,nums,n,m,s)