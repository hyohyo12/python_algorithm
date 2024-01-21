def can_be_s(s:list[str],t:list[str])->bool:
    while len(s) != len(t):
        tmp = t.pop()
        if tmp == 'B':
            t = t[::-1]
    if s == t:
        return True
    return False



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    s = list(input().strip())
    t = list(input().strip())
    
    if can_be_s(s,t):
        print(1)
    else:
        print(0)