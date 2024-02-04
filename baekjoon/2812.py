import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n,k = map(int,input().split())
    seq = list(input().strip())
    stack = []
    for num in seq:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    print(''.join(stack[:len(stack)-k]))