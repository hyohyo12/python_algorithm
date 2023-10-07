# 15720 카우버거
import sys
input = sys.stdin.readline

firstLine = list(map(int,input().split())) # 첫 줄 B,C,D를 저장할 리스트
amount = [] # 금액을 저장할 리스트
oldSum = 0 # 할인 전 금액을 저장할 리스트

for i in range(3):# 금액 입력 받기
    listA = list(map(int,input().split())) # 입력받아 listA 리스트에 저장
    listA = sorted(listA,reverse=True) # 내림차순으로 정렬
    amount.append(listA) # 2차원리스트 형태로 amount 에 저장
    oldSum += sum(amount[i]) # 할인 전 금액에 더하기
print(oldSum) # 할인 전 가격 출력

ans = 0 # 정답을 저장할 변수

for i in range(max(firstLine)): # 리스트 요소 더할 리스트
    try:
        temp = 0 # 햄버거, 감튀, 음료수 를 합해 저장할 임시 변수
        temp += amount[0][i] # 정렬 했으므로 앞이 햄버거 중 가장 큰 값!
        temp += amount[1][i] # 정렬 했으므로 앞이 감튀 중 가장 큰 값!
        temp += amount[2][i] # 정렬 했으므로 앞이 음료수 중 가장 큰 값!
    except:
        break # 만약 인덱스 에러가 나면 리스트의 값이 없다는 뜻 즉 햄버거 or 감튀 or 음료수 중 값이 비었다는 뜻이므로 반복문 종료
    ans += temp # 정답 변수에 임시 변수에 있는 값 저장

oldSum -= ans # 이전 값에 답 변수를 빼면 세트가 되지 않는 값이 도출
ans *= 0.9 # 세트가 완성된 변수에 0.9 곱하면 할인 된 값
ans+=oldSum # 세트가 완성되지 않은 변수 + 완성되고 할인 된 값
print(int(ans)) #출 력