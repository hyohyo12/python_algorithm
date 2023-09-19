n = int(input())
res = 0
while n >= 0:
    if n%5 == 0:
        res += n // 5
        break
    else:
        if n < 2:
            res = -1
            break
        else:
            res += 1
            n -= 2
print(res)