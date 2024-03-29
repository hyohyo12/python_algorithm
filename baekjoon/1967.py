import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(tree:list[list[int]],cur_node,cur_cost):
    for next_node,next_cost in tree[cur_node]:
        if visited[next_node] == -1:
            visited[next_node] = cur_cost+next_cost
            dfs(tree,next_node,cur_cost+next_cost)

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        parent,cur,weight = map(int,input().split())
        tree[parent].append((cur,weight))
        tree[cur].append((parent,weight))
        
    visited = [-1 for _ in range(n+1)]
    visited[1] = 0
    dfs(tree,1,0)
    
    node,tmp = 0,0
    for idx,cost in enumerate(visited):
        if cost > tmp:
            node = idx
            tmp = cost
    visited = [-1 for _ in range(n+1)]
    visited[node] = 0
    dfs(tree,node,0)
    print(max(visited))