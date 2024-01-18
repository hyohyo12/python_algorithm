def tot_line(seq:list[list[int]],n:int)->int:
    line = 0
    seq.sort()
    left = seq[0][0]
    right = seq[0][1]
    
    for i in range(1,n):
        if seq[i][1] <= right:
            continue
        elif seq[i][0] <= right and seq[i][1] >right:
            right = seq[i][1]
        elif seq[i][0] > right:
            line += right - left
            left = seq[i][0]
            right = seq[i][1]
    line += right - left
    return line
            


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    seq = []
    n = int(input())
    for i in range(n):
        seq.append(list(map(int,input().split())))
    print(tot_line(seq,n))