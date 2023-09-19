import sys
def FindDigit(num):
    one = 11 #1 로 구성된 자연수 ex) 1,11,111,1111 이런식으로
    count =100 # one 변수가 11 -> 111 -> 1111 로 변할 수 있도록 만든 변수
    digitCounter = 2 #자릿 수 세어 줄 변수
    if num == 1: #그냥 1인 경우
        return 1# 그냥 1 리턴
    while one%num != 0: # 1로 구성된 자연수가 num 으로 나누어 지지 않을 동안-> num으로 나눠지면 while 문 빠져나감
        one+=count #11 + 100 해서 111 밑에 100*10 되면 1000 -> 1000+111 -> 1111 이런식으로 한 자리씩 늘어나게 함
        count=count*10 # 위에 설명
        digitCounter+=1# 자릿 수 하나 증가
    return digitCounter #해서 나온 자릿 수 리런
if __name__ == '__main__': #메인
    while 1:# 무한 루프
        try:
            n = int(sys.stdin.readline()) # n 입력
            print(FindDigit(n)) # FindDigit 함수에 돌리고 리턴값 출력
        except:
            break