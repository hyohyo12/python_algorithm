import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    seq = []
    for _ in range(n):
        seq.append(list(map(int,input().split())))
    for i in range(n-2,-1,-1):
        for j in range(len(seq[i])):
            seq[i][j] += max(seq[i+1][j],seq[i+1][j+1])
    print(seq[0][0])