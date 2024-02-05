import sys
from collections import deque
input = sys.stdin.readline



if __name__ == "__main__":
    s = deque(list(input().strip()))
    
    ans = deque([s[0]])
    s.popleft()
    
    while s:
        x = s.popleft()
        if x >= ans[-1]:
            ans.append(x)
        else:
            if ans[0] >= x:
                ans.appendleft(x)
            else:
                ans.append(x)
    print(''.join(ans))