def dfs(visited,nums,n,m,tmp_stack,start):
    if len(tmp_stack) == m:
        print(" ".join(map(str,tmp_stack)))
    for i in range(start,n):
        if not visited[i]:
            tmp_stack.append(nums[i])
            visited[i] = True
            dfs(visited,nums,n,m,tmp_stack,i)
            visited[i] = False
            tmp_stack.pop()
if __name__ == "__main__":
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    visited = [False] * n
    s = []
    dfs(visited,nums,n,m,s,0)