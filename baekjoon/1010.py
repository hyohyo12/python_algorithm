bridge = [[1] * 31 for i in range(31)]
for i in range(31):
    bridge[1][i] = i
for i in range(2,31):
    for j in range(i+1,31):
        bridge[i][j] = bridge[i-1][j-1] + bridge[i][j-1]
        
for i in range(int(input())):
    n,m = map(int,input().split())
    print(bridge[n][m])