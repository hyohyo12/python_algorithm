def minimum_walk(seq:list[int],m:int,n:int)->int:
    positive = []
    negative = []
    distance = []
    
    def divide():
        for i in seq:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
    divide()
    
    positive.sort(reverse=True)
    negative.sort()
    
    for i in range(0,len(positive),m):
        distance.append(positive[i])
        
    # if len(positive)%m:
    #     distance.append(positive[-1])
        
    for j in range(0,len(negative),m):
        distance.append(abs(negative[j]))
        
    # if len(negative)%m:
    #     distance.append(abs(negative[-1]))
    
    distance.sort()
    res = distance.pop()
    res += sum(distance)*2
    return res


if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    
    n,m = map(int,read().split())
    seq = tuple(map(int,read().split()))
    
    print(minimum_walk(seq,m,n))