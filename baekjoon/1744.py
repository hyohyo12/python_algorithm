def maximum_sum(plus_seq:list[int],minus_seq:list[int])->int:
    result = 0
    plus_seq.sort(reverse=True)
    minus_seq.sort()
    for i in range(0,len(plus_seq),2):
        if i+1 >= len(plus_seq):
            result += plus_seq[i]
        else:
            result += (plus_seq[i]*plus_seq[i+1])
    
    for i in range(0,len(minus_seq),2):
        if i+1 >= len(minus_seq):
            result += minus_seq[i]
        else:
            result += (minus_seq[i]*minus_seq[i+1])
    return result
            
        
    

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    res = 0
    plus_seq = []
    minus_seq = []
    n = int(input())
    for i in range(n):
        num = int(input())
        if num > 1:
            plus_seq.append(num)
        elif num <= 0:
            minus_seq.append(num)
        else: res+=1
    print(res+maximum_sum(plus_seq,minus_seq))