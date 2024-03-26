import sys
input = sys.stdin.readline

#정답 함수
def word_math(seq:list[int])->int:
    #결과(각 알파벳에 숫자를 부여하고 더한 값)
    res = 0
    #각 알파벳의 자릿 수를 저장할 리스트
    alpha = [0 for _ in range(26)]
    #seq내에 모든 단어 탐색
    for s in seq:
        #c는 자릿 수 계산하기 위한 변수 1,10,100,1000
        c = 1
        for char in s[::-1]:
            #단어 뒤에서부터 자릿수 채워나감
            alpha[ord(char)-65] += c
            c *= 10
    #각 알파벳의 자릿수에 대해 오름차순 정렬
    alpha.sort(reverse=True)
    #res(정답 변수)에 해당하는 숫자 입력(오름차순 정렬됐으므로 9부터 삽입)
    for i in range(9):
        res += alpha[i] * (9-i)
    #res(정답)리턴
    return res
if __name__ == "__main__":
    #입력
    #단어 수
    n = int(input())
    #단어 입력
    seq = [input().rstrip() for _ in range(n)]
    #함수 실행 및 결과 출력
    print(word_math(seq))