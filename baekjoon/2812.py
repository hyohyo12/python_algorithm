import sys
input = sys.stdin.readline

if __name__ == "__main__":
    #입력
    n,k = map(int,input().split())
    seq = list(input().strip())
    
    stack = [] #숫자를 저장할 스택
    
    for num in seq:#순자를 탐색하여
        while stack and num > stack[-1] and k > 0: #stack에 숫자가 있고 스택에 위 숫자가 현재 숫자 보다 크고 k(숫자를 지울 횟수)가 0보다 클 때까지
            stack.pop() #스택에서 지운다
            k -= 1 
        stack.append(num) #현재숫자 스택에 추가
    print(''.join(stack[:len(stack)-k])) #탐색을 마치더라도 k가 0이 아닐 수 있음 그래서 빼주고 출력한다.
    
    

