import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    pos = []
    neg = []
    for _ in range(n):
        x,p = map(int,input().split())
        if x >= 0:
            neg.append((x,p))
        else:pos.append((x,p))
    neg.sort(reverse=True)
    pos.sort()
    
    count = 0
    if len(neg) and len(pos):
        if abs(neg[-1]) > pos[-1]:
            neg.pop()
        else:pos.pop()
    elif len(neg) >= 1 and len(pos) == 0:
        neg.pop()
    elif len(neg) == 0 and len(pos) >= 1:
        pos.pop()
    
    
