import sys
from collections import deque
input = sys.stdin.readline
def can_live(seq:list[int],MK:int,ML:int,C:int,L:int)->bool:
    attak = [0]
    for idx in range(1,L+1):
        ml = max(0,idx-ML)
        damage = attak[idx-1] - attak[ml]
        if damage + MK >= seq[idx]:
            attak.append(attak[idx-1]+MK)
        else:
            if C > 0:
                C -= 1
                attak.append(attak[idx-1])
            else:
                return False
    return True
    # damage = 0
    # for idx in range(1,L+1):
    #     if damage < (MK*ML):
    #         if damage + MK >= seq[idx]:
    #             damage += MK
    #             continue
    #         else:
    #             if C > 0:
    #                 C -= 1
    #                 damage = max(0,damage-MK)
    #                 continue
    #             else:
    #                 return False
    #     else:
    #         if damage < seq[idx]:
    #             if C > 0:
    #                 C -= 1
    #                 damage = max(0,damage-((ML-1)*MK))
    #                 continue
    #             else:
    #                 return False
    # return True



if __name__ == "__main__":
    L = int(input())
    ML,MK = map(int,input().split())
    C = int(input())
    seq = [0]+[int(input()) for _ in range(L)]
    
    print('YES' if can_live(seq,MK,ML,C,L) else 'NO')