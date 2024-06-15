import sys
input = sys.stdin.readline


#메인함수
def main():
    #초기화
    #사이트의 주소와 비밀번호 쌍으로 저장할 딕셔너리
    passwd = {}
    #입력
    #n -> 사이트의 개수, m -> 찾으려는 사이트의 주소
    n,m = map(int,input().split())
    
    #n개의 사이트 만큼 주소와 비밀번호 쌍으로 입력
    for _ in range(n):
        site,pw = input().strip().split()
        passwd[site] = pw
    
    #m개의 사이트에 대한 비밀번호 출력
    for _ in range(m):
        print(passwd[input().strip()])


if __name__ == "__main__":
    main()