def make_nums(nums,visited,n,m):
    if len(nums) == m:
        print(*nums)
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            nums.append(i)
            make_nums(nums,visited,n,m)
            visited[i] = False
            nums.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    visited = [False] *(n+1)
    make_nums([],visited,n,m)