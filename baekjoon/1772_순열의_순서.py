import sys
input = sys.stdin.readline

def my_permutation(n:int,depth:int,cur:list[int],visited:list[int])->list:
    global seq
    if depth == n:
        seq.append(cur[:])
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        cur.append(i)
        visited[i] = True
        my_permutation(n,depth+1,cur,visited)
        visited[i] = False
        cur.pop()

def main():
    global seq
    #입력
    #n -> 1부터 n까지의 수
    n = int(input())
    #tmp[0] -> 문제의 번호, 나머지 -> 문제에 필요한 정보(k번째 수열 또는 수열)
    tmp = list(map(int,input().split()))
    my_permutation(n,0,[],[False for _ in range(n+1)])
    #k번째 수열을 구하는 문제
    if tmp[0] == 1:
        print(*seq[tmp[1]-1])
        return
    #어떠한 수열의 번호를 구하는 문제
    else:
        print(seq.index(tmp[1:]) + 1)
        return
if __name__ == "__main__":
    seq = []
    main()