import sys
input = sys.stdin.readline

def s_can_be_t(s:str,t:list[str]):
    while len(s) != len(t):
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t.reverse()
    return 1 if s == ''.join(t) else 0


if __name__ == "__main__":
    s = input().rstrip()
    t = list(input().rstrip())
    
    print(s_can_be_t(s,t))