import sys
input = sys.stdin.readline

parents = []

#union - find
def find(x : int):
    #x 가 parents의 x번 인덱스 값과 같다는 뜻 -> 부모 노드가 없다
    if x == parents[x]:
        #자신을 리턴을 한다
        return x
    #해당 값의 최고 부모 노드를 계속 갱신한다.
    parents[x] = find(parents[x])
    #x의 최고 부모 노드를 리턴한다
    return parents[x]

def union(u:int,v:int):
    #u의 부모노드와 v의 부모노드를 찾는다
    u,v = find(u),find(v)
    #v의 부모 노드를 u로 설정한다
    parents[v] = u

#메인함수
def main():
    global parents
    #게이트 수G, 비행기 수 P를 입력
    G = int(input())
    P = int(input())
    #결과를 저장할 변수
    res = 0
    parents = [i for i in range(G + 1)]
    planes = [int(input()) for _ in range(P)]
    #planes 탐색
    for plane in planes:
        #현재 비행기의 게이트(부모노드) 를 찾는다.
        gate = find(plane)
        #해당 게이트의 부모노드가 0이라면 해당 비행기가 도킹할 수 있는 번호부터 1번까지 모두 찼다는 뜻이므로 break
        if gate == 0:
            break
        #도킹할 수 있는 게이트를 gate의 왼쪽(하나 작은) 곳을 부모노드로 union한다. -> 다음 비행기의 게이트로 못쓰고 다음 게이트를 사용하게 하기 위함.
        union(gate-1,gate)
        #결과값 + 1
        res += 1
    print(res)
    
if __name__ == "__main__":
    main()