import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def multiply(A: list[list[int]],B:list[list[int]])-> list[list[int]]:
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for cow in range(n):
            tmp = 0
            for i in range(n):
                tmp += A[row][i] * B[i][cow]
            result[row][cow] = tmp % 1000
    return result

def power(matrix:list[list[int]],b:int):
    if b == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] %= 1000
        return matrix
    
    tmp = power(matrix,b//2)
    
    if b % 2:
        return multiply(multiply(tmp,tmp),matrix)
    else:
        return multiply(tmp,tmp)


if __name__ == "__main__":
    n,b = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    result = power(board,b)
    for seq in result:
        print(*seq)