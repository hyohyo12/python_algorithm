import sys
input = sys.stdin.readline



if __name__ == "__main__":
    bracket = list(input().rstrip())
    res = 0
    stack = []
    tmp = 1
    for i,c in enumerate(bracket):
        if c == '(':
            stack.append(c);tmp *= 2
        elif c == '[':
            stack.append(c);tmp*=3
        elif c == ')':
            if not stack or stack[-1] != '(':
                res=0;break
            if bracket[i-1] == '(':
                res += tmp
            stack.pop()
            tmp //= 2
        else:
            if not stack or stack[-1] != '[':
                res = 0;break
            if bracket[i-1] == '[':
                res += tmp
            stack.pop()
            tmp //= 3
    print(0 if stack else res)