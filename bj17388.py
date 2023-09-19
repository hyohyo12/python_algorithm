s,k,h=map(int,input().split())
if s+h+k>100:
    print("OK")
else:
    if min(s,h,k)==s:
        print("Soongsil")
    elif min(s,h,k)==h:
        print("Hanyang")
    elif min(s,h,k)==k:
        print("Korea")