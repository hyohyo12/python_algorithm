case = 0
while True:
    case+=1
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    a = v//p
    b = v%p
    if l < b:
        b = l
    print("Case {0}: {1}".format(case,a*l+b))