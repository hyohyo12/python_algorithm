from collections import deque
def fire(seq:list[list[str]],r: int,c: int,j_start: tuple,f_q, visited_f,visited_j):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def bfs_f():
        while f_q:
            f_y,f_x = f_q.popleft()
            for x,y in zip(dx,dy):
                nx = x+f_x
                ny = y+f_y
                if 0 <= nx < len(seq[0]) and 0 <= ny < len(seq):
                    if not visited_f[ny][nx]:
                        if seq[ny][nx] != '#':
                            visited_f[ny][nx] = visited_f[f_y][f_x] + 1
                            seq[ny][nx] = 'F'
                            f_q.append((ny,nx))
    bfs_f()
    
    q = deque([j_start])
    while q:
        j_y,j_x = q.popleft()
        for x,y in zip(dx,dy):
            nx = x+j_x
            ny = y+j_y
            if 0 <= nx < len(seq[0]) and 0 <= ny < len(seq):
                if not visited_j[ny][nx] and seq[ny][nx] != '#':
                        if not visited_f[ny][nx] or (visited_f[ny][nx] > visited_j[j_y][j_x]+1):
                            q.append((ny,nx))
                            visited_j[ny][nx] = visited_j[j_y][j_x] + 1
            else:
                return visited_j[j_y][j_x]
    return 'IMPOSSIBLE'


if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    
    r,c = map(int,read().split())
    seq = [list(read().strip()) for _ in range(r)]
    f_q = deque([])
    visited_f = [[0 for _ in range(c)] for _ in range(r)]
    visited_j = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if seq[i][j] == 'J':
                j_start = (i,j)
                visited_j[i][j] = 1
            if seq[i][j] == 'F':
                f_q.append((i,j))
                visited_f[i][j] = 1
    print(fire(seq,r,c,j_start,f_q,visited_f,visited_j))