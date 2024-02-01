import sys
input = sys.stdin.readline
def indent(n:int,t_seq: list[int],r_seq: list[int])->int:
    dif = []
    ans = 0
    minus = False
    plus = False
    zero = False
    for t,r in zip(t_seq,r_seq):
        dif.append(r-t)
    for i in range(n-1,-1,-1):
        if i == (n-1):
            if dif[i] < 0:
                ans += abs(dif[i])
                minus = True
            elif dif[i] > 0:
                ans += dif[i]
                plus = True
            elif dif[i] == 0:
                zero = True
        else:
            if minus:
                if dif[i] < 0:
                    if abs(dif[i]) < abs(dif[i+1]):
                        continue
                    else:
                        ans += abs(abs(dif[i])-abs(dif[i+1]))
                        continue
                elif dif[i] > 0:
                    ans += dif[i]
                    minus = False
                    plus =True
                else:
                    minus = False
                    zero = True
            elif plus:
                if dif[i] < 0:
                    ans += abs(dif[i])
                    minus = True
                    plus = False
                elif dif[i] > 0:
                    if dif[i+1] < dif[i]:
                        ans += abs(dif[i] - dif[i+1])
                    else:
                        continue
                else:
                    plus = False
                    zero = True
            elif zero:
                if dif[i] < 0:
                    ans += abs(dif[i])
                    minus = True
                    zero = False
                elif dif[i] > 0:
                    ans += dif[i]
                    plus = True
                    zero = False
    return ans
if __name__ == "__main__":
    n = int(input())
    t_seq = list(map(int,input().split()))
    r_seq = list(map(int,input().split()))
    
    print(indent(n,t_seq,r_seq))