def get_tape(l,pipe):
    start = pipe[0]
    count = 1
    for i in pipe[1:]:
        if i in range(start,start+l):
            continue
        else:
            start = i
            count += 1
    return count
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n,l = map(int,input().split())
    pipe = list(map(int,input().split()))
    pipe.sort()
    print(get_tape(l,pipe))