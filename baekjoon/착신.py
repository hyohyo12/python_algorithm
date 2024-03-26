import sys
input = sys.stdin.readline



if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    
    count = 0
    for idx,v in enumerate(seq):
        if v == (idx+1):
            seq[idx] = v+1 if idx < (n-1) else 1
            count += 1
    print(count)
    if count >= 1:
        print(*seq)