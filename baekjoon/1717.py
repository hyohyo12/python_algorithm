import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
parents = []
def find(x : int):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(u:int, v:int):
    u,v = find(u),find(v)
    if u < v:
        parents[v] = u
    else:
        parents[u] = v


def main():
    global parents
    n,m = map(int,input().split())
    parents = [i for i in range(n + 1)]
    for _ in range(m):
        c,a,b = map(int,input().split())
        if c == 0:
            union(a,b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()