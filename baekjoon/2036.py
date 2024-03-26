def max_score(pos:list[int],neg:list[int],zero: list[int])->int:
    res = 0
    if len(pos) % 2 and len(neg) % 2: #홀수
        for i in range(0,len(pos)-1,2):
            res += max(pos[i]*pos[i+1],pos[i]+pos[i+1])
        res += pos[-1]
        for i in range(0,len(neg)-1,2):
            res += max(neg[i]*neg[i+1],neg[i]+neg[i+1])
        if len(zero) == 0:
            res += neg[-1]

    elif len(pos) % 2 and (len(neg) % 2 == 0):
        for i in range(0,len(pos)-1,2):
            res +=max(pos[i]*pos[i+1],pos[i]+pos[i+1])
            
        for i in range(0,len(neg),2):
            res += max(neg[i]*neg[i+1],neg[i]+neg[i+1])
        res += pos[-1]


    elif (len(pos) % 2 == 0) and len(neg) % 2:
        for i in range(0,len(neg)-1,2):
            res += max(neg[i]*neg[i+1],neg[i]+neg[i+1])
            
        for i in range(0,len(pos),2):
            res +=max(pos[i]*pos[i+1],pos[i]+pos[i+1])
        if len(zero) == 0:
            res += neg[-1]


    else:
        for i in range(0,len(neg),2):
            res += max(neg[i]*neg[i+1],neg[i]+neg[i+1])
        for i in range(0,len(pos),2):
            res += max(pos[i]*pos[i+1],pos[i]+pos[i+1])
    return res



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    positive = []
    negative = []
    zero = []
    for _ in range(n):
        num = int(input())
        if num < 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
        else:
            zero.append(num)
    negative.sort()
    positive.sort(reverse=True)
    print(max_score(positive,negative,zero))