def buy_one(idx:int):
    global ans
    ans += seq[idx] * 3
    
def buy_two(idx:int):
    global ans
    m = min(seq[idx:idx+2])
    seq[idx] -= m
    seq[idx+1] -= m
    ans += m * 5
def buy_three(idx:int):
    global ans
    m = min(seq[idx:idx+2])
    seq[idx] -= m
    seq[idx+1] -= m
    seq[idx+2] -= m
    ans +=  m * 7


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    ans = 0
    n = int(input())
    seq = list(map(int,input().split())) + [0,0]
    for i in range(0,n):
        if seq[i+1] > seq[i+2]:
            m = min(seq[i],seq[i+1] - seq[i+2])
            seq[i] -= m
            seq[i+1] -= m
            ans += (m*5)
            buy_three(i)
            buy_one(i)
        else:
            buy_three(i)
            buy_two(i)
            buy_one(i)
    print(ans)
    