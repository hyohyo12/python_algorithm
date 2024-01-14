A=[list(map(int,input().split()))for _ in range(9)]
A_Max = 0
max_Col=0
max_Row=0
for col in range(9):
    for row in range(9):
        if(A_Max<=A[col][row]):
            A_Max = A[col][row]
            max_Col = col
            max_Row = row
print(A_Max)
print("{0} {1}".format(max_Col+1,max_Row+1))