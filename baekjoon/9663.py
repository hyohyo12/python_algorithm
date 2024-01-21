def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(i-x) == abs(row[i]-row[x]):
            return False
    return True
def n_queen(x):
    global ans
    if x == n:
        ans+=1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queen(x+1)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    ans = 0
    n = int(input())
    row = [0] * (n)
    n_queen(0)
    print(ans)