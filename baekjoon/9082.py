def nums_mine(seq: list[int],n: int)-> int:
    mine = 0
    for i in range(n):
        if i == 0:
            if seq[0] != 0 and seq[1] != 0:
                seq[0] -= 1
                seq[1] -= 1
                mine += 1
        elif i == n-1:
            if seq[i-1] != 0 and seq[i] != 0:
                seq[i-1] -= 1
                seq[i] -= 1
                mine += 1
        else:
            if seq[i] != 0 and seq[i-1] != 0 and seq[i+1] != 0:
                seq[i] -= 1
                seq[i-1] -= 1
                seq[i+1] -= 1
                mine += 1
    return mine

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    for i in range(int(input())):
        n = int(input())
        seq = list(map(int,input().strip()))
        mine = input().strip()
        print(nums_mine(seq,n))