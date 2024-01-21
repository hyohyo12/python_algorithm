# def find_combinations(seq:list[int]):
#     import itertools
#     return list(map(list,itertools.combinations(seq,6)))

def find_combinations(seq:list[int])->list[list[int]]:
    result = []
    def dfs(start,cur):
        if len(cur) == 6:
            result.append(cur[:])
            return
        for i in range(start,len(seq)):
            cur.append(seq[i])
            dfs(i+1,cur)
            cur.pop()
    dfs(0,[])
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    while True:
        n,*seq = list(map(int,input().split()))
        if n == 0:
            break
        for i in find_combinations(seq):
            print(*i)
        print()