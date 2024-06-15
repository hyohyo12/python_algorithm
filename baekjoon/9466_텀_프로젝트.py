import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(idx):
    global seq
    global cycle
    global res
    global visited
    visited[idx] = True
    cycle.append(idx)
    num = seq[idx]
    if visited[num]:
        if num in cycle:
            res += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

def main():
    for _ in range(int(input())):
        global seq
        global cycle
        global res
        global visited
        res = []
        n = int(input())
        visited = [0] + [False for _ in range(n)]
        seq = [0] + list(map(int,input().split()))
        for i in range(1,n+1):
            if not visited[i]:
                cycle = []
                dfs(i)
        print(n - len(res))

if __name__  == "__main__":
    seq = []
    cycle = []
    res = []
    visited = []
    main()
