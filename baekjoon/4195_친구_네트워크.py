import sys
input = sys.stdin.readline


class union_find:
    def __init__(self):
        #union-find 각각 root를 딕셔너리로 선언
        self.root = {}
        #각 노드에 대해 depth를 저장할 딕셔너리
        self.depth = {}
    
    #find 함수
    def find(self,x):
        #딕셔너리에 x가 없다면 새로 추가
        if x not in self.root:
            self.root[x] = x
            self.depth[x] = 1
        
        #루트 노드 찾기
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    #집합으로 묶는 함수
    def union(self,x,y):
        #x와 y의 root노드 찾기
        rootX = self.find(x)
        rootY = self.find(y)
        #같은 집합에 속하지 않을 때만 연결
        if rootX != rootY:
            #깊이
            self.depth[rootX] += self.depth[rootY]
            self.root[rootY] = rootX
        #현재 친구 관계의 네트워크 깊이 출력
        print(self.depth[rootX])


#메인 함수
def main():
    #테스트 케이스만큼 반복
    for _ in range(int(input())):
        #입력
        #친구 관계의 개수 n 
        n = int(input())
        #union_find 객체 생성
        uf = union_find()
        #친구 관계 수 만큼 반복
        for _ in range(n):
            #x <-> y 관계
            x,y = input().strip().split()
            #집합 연결
            uf.union(x,y)



if __name__ == "__main__":
    main()