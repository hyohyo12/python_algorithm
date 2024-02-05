import sys
input = sys.stdin.readline

def get_steps(seq:list[int],m:int)->int:
    coords = []
    pos = []
    neg = []
    
    for i in seq:
        if i > 0 : pos.append(i)
        else : neg.append(i)
    
    pos.sort(reverse=True)
    neg.sort()
    
    for i in range(0,len(pos),m):
        coords.append(pos[i])
    
    for i in range(0,len(neg),m):
        coords.append(abs(neg[i]))
    
    coords.sort()
    
    steps = coords.pop()
    steps += sum(coords) * 2
    
    return steps

if __name__ == "__main__":
    n,m = map(int,input().split())
    seq = list(map(int,input().split()))
    
    print(get_steps(seq,m))