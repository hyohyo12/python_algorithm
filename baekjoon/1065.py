n = int(input())

count = n

if n > 99:
    count = 99
    for i in range(100,n+1):
        arr = list(map(int,list(str(i))))
        if arr[1] - arr[0] == arr[2] - arr[1]:
            count += 1
print(count)