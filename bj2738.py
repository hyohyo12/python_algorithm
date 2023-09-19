N,M = map(int,input().split())
A =[list(map(int,input().split())) for j in range(N)]
B =[list(map(int,input().split())) for j in range(N)]
result=[list(0 for i in range(M)) for j in range(N)]
for i in range(0,N,1):
    for j in range(0,M,1):
        result[i][j] = A[i][j]+B[i][j]
for i in range(0,N,1):
    for j in range(0,M,1):
        print("{0}".format(result[i][j]),end=" ")
        if(j==M-1):
            print("")