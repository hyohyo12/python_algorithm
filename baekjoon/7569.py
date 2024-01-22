from collections import deque
def tomato(seq:list[list[int]],h:int,n:int,m:int)->int:
    dx,dy,dz= [0,0,1,-1,0,0],[1,-1,0,0,0,0],[0,0,0,0,1,-1]
    start = deque([])
    def bfs(start):
        day = 0
        while start:
            day += 1
            for _ in range(len(start)):
                cur_z,cur_y,cur_x = start.popleft()
                for x,y,z in zip(dx,dy,dz):
                    nx,ny,nz = cur_x + x, cur_y + y, cur_z + z
                    if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                        if seq[nz][ny][nx] == 0:
                            seq[nz][ny][nx] = 1
                            start.append((nz,ny,nx))
        return day
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if seq[i][j][k] == 1:
                    start.append((i,j,k))
    days = bfs(start)
    for z in range(h):
        for y in range(n):
            if 0 in seq[z][y]:
                return -1
    return days - 1

if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    m,n,h = map(int,read().split())
    seq = [[list(map(int,read().split())) for _ in range(n)] for _ in range(h)]
    print(tomato(seq,h,n,m))