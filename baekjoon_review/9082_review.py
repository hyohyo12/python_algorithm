import sys
input = sys.stdin.readline


def find_mine(n:int,n_seq:list[int],s_seq:list[str])->int:
    mine = 0 #지뢰 수(정답) 을 저장할 변수
    for i in range(n): #지뢰가 확실히 있는 곳 우선 카운트
        if s_seq[i] == '*': #만약 '*'(지뢰가 확실히 있는 곳) 이라면
            mine += 1 #지뢰 수 + 1
            n_seq[i] -= 1 #현재 지뢰 수 리스트에서 현재 지뢰에 대한 처리를 위해 - 1
            if i == 0: #인덱스 에러 방지로 0이라면
                n_seq[i+1] -= 1 #현재 i인덱스가 0이므로 전 인덱스는 존재하지 않으므로 i+1 만 - 1
            elif i == n-1: #만약 인덱스가 끝이라면
                n_seq[i-1] -= 1 #현재 i인덱스가 마지막이므로 다음 인덱스는 존재하지 않으므로 i-1 만 -1
            else: #그 외 (앞 뒤 인덱스가 존재하는 경우)
                n_seq[i-1] -= 1 #i-1,i+1(앞 뒤) 인덱스 모두 삭제
                n_seq[i+1] -= 1 #i번 인덱스는 공통으로 삭제해야하므로 위에 n_seq[i] -= 1이 역할함
    for idx in range(n): #이번엔 모든 '#'에 대해 탐색
        if idx == 0: #인덱스 에러 방지(0번 인덱스는 전 인덱스 존재하지 않으므로 현재 인덱스,현재 인덱스+1 번만 검증)
            if s_seq[idx] == '#' and n_seq[idx+1] != 0 and n_seq[idx] != 0: #현재 idx번째 인덱스가 검증이 되지 않았고 현재 인덱스, 다음 인덱스가 0이 아닌경우
                n_seq[idx+1] -= 1 #지뢰가 있다는 뜻으로 두 인덱스 모두 - 1
                n_seq[idx] -= 1 
                mine += 1 #지뢰 수 + 1
        elif idx == n-1:#인덱스 에러방지(마지막 인덱스는 다음 인덱스가 존재하지 않으므로 현재 인덱스 -1 만 검증)
            if s_seq[idx] == '#' and n_seq[idx-1] != 0 and n_seq[idx] != 0: #위와 동일
                n_seq[idx-1] -= 1 
                n_seq[idx] -= 1
                mine += 1
        else: #처음,마지막 인덱스를 제외한 나머지 부분
            if s_seq[idx] == '#' and n_seq[idx] != 0 and n_seq[idx-1] != 0 and n_seq[idx+1]:#현재, 현재-1, 현재 +1 모두 검증
                n_seq[idx-1] -= 1
                n_seq[idx+1] -= 1
                n_seq[idx] -= 1
                mine += 1
    return mine


if __name__ == "__main__":
    t = int(input()) #테스트 케이스 수
    for _ in range(t):
        n = int(input()) #배열 크기
        
        n_seq = list(map(int,input().strip())) #주변 지뢰 수를 저장할 리스트
        s_seq = list(input().strip()) #주변 지뢰 여부 저장할 문자 리스트 '#' -> 아직 지뢰가 있는지 밝혀지지 않는곳 '*' -> 지뢰가 확실히 있는곳
        
        print(find_mine(n,n_seq,s_seq))