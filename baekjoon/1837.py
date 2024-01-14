p , k = map(int,input().split())
for i in range(2,k+1):
    if p % i == 0:
        print("BAD {0}".format(i))
        break
else:
    print("GOOD")