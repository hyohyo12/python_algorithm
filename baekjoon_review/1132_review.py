import sys
input = sys.stdin.readline


if __name__ == "__main__":
    ans = 0 #정답 저장 변수
    n = int(input()) #단어 수 입력
    seq = [[0,False] for _ in range(10)] #A-J 까지 데이터를 2중리스트로 구성 [i][0] 은 자릿수 [i][1] 은 문제 조건에 맞추기 위해(앞자리엔 0이 올 수 없다) 검증할 수 있는 boolean
    
    for _ in range(n): #단어 수 만큼 반복
        s = input().strip() #단어 입력
        
        seq[ord(s[0])-65][1] = True #첫번째 자리는 True로 변환
        m = 1 #각 자릿수를 계산할 임시 변수
        for i in range(len(s)-1,-1,-1): #각자리 수 비교를 위해 거꾸로 탐색
            seq[ord(s[i])-65][0] += m # 각 알파벳에 대한 자릿수 저장
            m *= 10 #각 자릿수를 계산하기위해 *10
    seq.sort(reverse=True) #각자릿수에 대해 오름차순 정렬
    if seq[-1][1]: #마지막 알파벳(자릿 수가 제일 작은 값) 이 앞에 나온적이 있다면
        for i in range(8,-1,-1): #뒤에서 앞으로 탐색(오름차순이기 때문에)
            if not seq[i][1]: #첫번째로 나온적이 없다면
                del seq[i] #해당 인덱스 삭제 후
                break #바로 break(오름차순 정렬이기 때문에 제일 작은 자릿 수이자 앞으로 나온 적이 없는 변수이기때문에)
    for i in range(9): #알파벳에 대해 0~9 배정(오름차순 정렬이기 때문에 처음 인덱스가 제일 큰 자릿수)
        ans += (seq[i][0]*(9-i)) #9~1 각각 곱해주고 ans변수에 저장
    print(ans) #정답 변수 출력