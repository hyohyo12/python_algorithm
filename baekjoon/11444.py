

def mul(a: list[list[int]],b:list[list[int]]):
    tmp = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            num = 0
            for k in range(2):
                num += a[i][k]*b[k][j]
            tmp[i][j] = num % 1000000007
    return tmp

def power(mat: list[list[int]],n:int):
    if n == 1:
        return mat
    elif n % 2:
        return mul(power(mat,n-1),mat)
    else: return power(mul(mat,mat),n//2)

def main():
    n = int(input())
    mat = [[1,1],[1,0]]
    mat = power(mat,n)
    print(mat[0][1])
    
if __name__ == "__main__":
    main()