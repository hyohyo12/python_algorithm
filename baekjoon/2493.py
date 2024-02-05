import sys
input = sys.stdin.readline
def sol(n:int,seq:list[int])->int:
    stack = []
    ans_seq = [0 for _ in range(n)]
    for i in range(n):
        while stack:
            if stack[-1][0] > seq[i]:
                ans_seq[i] = stack[-1][1]+1
                break
            else:
                stack.pop()
        stack.append((seq[i],i))
    print(*ans_seq)


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    sol(n,seq)