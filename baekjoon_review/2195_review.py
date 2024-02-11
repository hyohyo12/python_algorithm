import sys
input = sys.stdin.readline
def sol(s:str,p:str)->int:
    p_index,count = 0,0 #문자열 p를 탐색할 p_index, 정답을 저장할 count
    while p_index < len(p): #문자열 p(새로운 문자열) 탐색
        s_index,max_len,cur = 0,0,0 #문자열 s(원본 문자열) 탐색할 s_index, 가장 긴 문자열의 길이 찾을 max_len,현재 공통 문자열 길이 저장할 변수 cur 
        while s_index < len(s) and p_index+cur < len(p):
            if s[s_index] == p[p_index+cur]: #원본 문자열의 문자열과 새로운 문자열의 문자 비교 cur로 증가
                cur += 1 #같다면 새로운 문자열(p)의 다음 문자 확인하기 위해 그리고 p 다음 문자 비교를 위해 cur 증가
                max_len = max(max_len,cur) #공통된 부분중 제일 긴 부분을 저장
            else: #다르다면 다시 새로운 문자열(p)에대해 처음부터 탐색해야하므로
                cur = 0 # cur 은 다시 0으로 설정
            s_index += 1 #s_index 탐색
        p_index += max_len #문자열 p 탐색 포인트를 제일 긴 공통 문자열의 길이만큼 증가
        count += 1 #최장 공통 부분 탐색후 정답 변수 + 1
    return count

if __name__ == "__main__":
    s = input().strip() #원본 문자열
    p = input().strip() #새로운 문자열
    
    print(sol(s,p))