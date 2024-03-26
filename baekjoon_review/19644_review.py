import sys
input = sys.stdin.readline

def can_live(l:int,ml:int,mk:int,c:int,z_seq:list[int])->bool:
    damage = [0 for _ in range(l+1)] #살상력 누적합을 저장할 리스트
    for i in range(1,l+1): #좀비들을 하나 하나 탐색하며
        tmp = max(i-ml,0) #현재 공격의 시작점 즉 언제부터 누적이 됐는지
        cur_damage = damage[i-1] - damage[tmp] #전 공격의 누적합에서 시작점을 빼서 현재 공격전의 누적 살상력을 저장
        if cur_damage+mk >= z_seq[i]: #누적 살상력에 현재 공격력 mk 를 더한값이 현재 좀비 체력보다 크거나 같으면 처리가능
            damage[i] = damage[i-1]+mk #누적 합 저장
            z_seq[i] = 0
        else: #누적 살상력 + 현재 살상력으로 처리 불가능하다면
            if c > 0: #수평 세열 지향성 지뢰(c) 가 남아있다면
                c -= 1 #사용
                damage[i] = damage[i-1] #총으로 살상하지 않았으므로 누적합(누적 살상력)은 전값과 같음
                z_seq[i] = 0 
            else: #지뢰가 없다면 처리 불가하므로
                return False # False 리턴
    return True #모두 순회하면 모두 처리했다는 뜻으로 True 리턴

if __name__ == "__main__":
    l = int(input()) #앞쪽 거리 l
    ml,mk = map(int,input().split()) #유효 사거리 ml ,살상력 mk
    c = int(input()) #수평 세열 지향성 지뢰(c)
    z_seq = [0] + [int(input()) for _ in range(l)] # 거리 l에 있는 좀비들의 체력
    
    print('YES' if can_live(l,ml,mk,c,z_seq) else 'NO')