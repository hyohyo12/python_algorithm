import sys
input = sys.stdin.readline

def pretty_code(req:list[int])->int:
    tab = abs(req[-1])
    
    for idx in range(len(req)-2,-1,-1):
        if req[idx+1] == 0:
            tab += abs(req[idx])
            continue
        if req[idx] < 0 and req[idx+1] <0 :
            if abs(req[idx]) > abs(req[idx+1]):
                tab += abs(abs(req[idx]) - abs(req[idx+1]))
        elif req[idx] > 0 and req[idx+1] > 0:
            if req[idx] <= req[idx+1]:
                continue
            else:
                tab += abs(req[idx]-req[idx+1])
        else:
            tab += abs(req[idx])
    return tab
    





if __name__ == "__main__":
    n = int(input())
    
    origin = list(map(int,input().split()))
    req = list(map(int,input().split()))
    
    for i,n in enumerate(origin):
        req[i] = req[i]-n
    print(pretty_code(req))