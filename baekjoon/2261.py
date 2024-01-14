import sys
input = sys.stdin.readline

def distance(a,b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    arr.sort()
    