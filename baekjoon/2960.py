import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n,k = map(int,input().split())
    counter = 0
    seq = [False for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            if not seq[j]:
                seq[j] = True
                counter += 1
                if counter == k:
                    print(j)
                    exit()