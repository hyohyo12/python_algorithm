import sys
input = sys.stdin.readline



if __name__ == "__main__":
    n,l = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    res = 0
    #가로
    for i in range(n):
        prev = board[i][0]
        same_count = 1
        high_flag = False
        for j in range(1,n):
            if prev == board[i][j]:
                same_count += 1
                if high_flag:
                    if same_count == l:
                        same_count = 0
                        high_flag = False
            elif prev != board[i][j]:
                if abs(prev-board[i][j]) >= 2:
                    break
                #올라감
                if prev-board[i][j] < 0:
                    if not high_flag and same_count >= l:
                        same_count = 1
                        prev = board[i][j]
                    else:
                        break
                #내려감
                else:
                    if not high_flag:
                        if l == 1:
                            same_count = 0
                            prev = board[i][j]
                            continue
                        high_flag = True
                        prev = board[i][j]
                        same_count = 1
                    else:break
        else:
            if high_flag:
                if same_count >= l:
                    res+=1
            else:res+=1
    #세로
    for i in range(n):
        prev = board[0][i]
        same_count = 1
        high_flag = False
        for j in range(1,n):
            if prev == board[j][i]:
                same_count += 1
                if high_flag:
                    if same_count == l:
                        same_count = 0
                        high_flag = False
            elif prev != board[j][i]:
                if abs(prev-board[j][i]) >= 2:
                    break
                #올라감
                if prev-board[j][i] < 0:
                    if not high_flag and same_count >= l:
                        same_count = 1
                        prev = board[j][i]
                    else:
                        break
                #내려감
                else:
                    if not high_flag:
                        if l == 1:
                            same_count = 0
                            prev = board[j][i]
                            continue
                        high_flag = True
                        prev = board[j][i]
                        same_count = 1
                    else:break
        else:
            if high_flag:
                if same_count >= l:
                    res+=1
            else:res+=1
    print(res)