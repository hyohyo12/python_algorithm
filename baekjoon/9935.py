import sys
input = sys.stdin.readline

if __name__ == "__main__":
    stack = []
    s = input().rstrip()
    bomb = input().rstrip()
    
    for i in s:
        stack.append(i)
        if len(stack) >= len(bomb):
            if ''.join(stack[-len(bomb):]) == bomb:
                for _ in range(len(bomb)):
                    stack.pop()
    print(''.join(stack) if len(stack) >= 1 else 'FRULA')