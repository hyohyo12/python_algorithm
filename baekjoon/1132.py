import sys
input = sys.stdin.readline


if __name__ == "__main__":
    ans = 0
    alpha = [[0,False] for _ in range(10)]
    n = int(input())

    for i in range(n):
        s = input().strip()
        alpha[ord(s[0])-65][1] = True
        m = 1
        for c in range(len(s)-1,-1,-1):
            alpha[ord(s[c])-65][0] += m
            m*=10
    alpha.sort(reverse=True)
    if alpha[9][1]: #끝값을 확인하는 이유 만약 True 면 확인해야함 위에 False 있는지 함부로 삭제 못하니깐
        for i in range(8,-1,-1): #끝값이라도 어느 숫자의 처음이 있다는 말로 숫자를 할당해야함 그래서 위에서부터 False 검사
            if not alpha[i][1]: #만약 False면 해당 값 지움 왜냐하면 어짜피 0이니깐 지움 처음 나오는게 젤 작은 값이므로0으로 하고
                del alpha[i] #Break임 
                break
    for i in range(9):
        ans += alpha[i][0] * (9-i)
    print(ans)
#위에 덧붙여서 뒤에 있는게 만약 False라면 제일 작은 값이므로 어짜피 위에 0~8번 인덱스까지 반복해서 알아서 걸러짐.
#만약 위에서 걸러져도 똑같이 최대 인덱스는 8이라서 모든 계산 가능.
