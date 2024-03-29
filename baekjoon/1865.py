import sys
inf = sys.maxsize
input = sys.stdin.readline

def bellman_ford(n:int,edge:list[tuple[int]])->list[list[int]]:
    distance = [inf for _ in range(n+1)]
    distance[1] = 0
    for i in range(n):
        for s,e,t in edge:
            if distance[s] != inf and distance[e] > t + distance[s]:
                distance[e] = t+distance[s]
                if i == n-1:
                    return True
    return False




def main():
    for _ in range(int(input())):
        n,m,w = map(int,input().split())
        edge = []
        for _ in range(m):
            s,e,t = map(int,input().split())
            edge.append((s,e,t))
            edge.append((e,s,t))
        for _ in range(w):
            s,e,t = map(int,input().split())
            edge.append((s,e,-t))
        print("YES" if bellman_ford(n,edge) else "NO")
if __name__ == "__main__":
    main()