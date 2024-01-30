if __name__ == "__main__":
    import sys
    from collections import Counter
    input = sys.stdin.readline
    
    n = int(input())
    
    seq = list(map(int,input().split()))
    seq_2 = sorted(list(set(seq)))
    
    dic = {seq_2[i] :i for i in range(len(seq_2))}
    for i in range(len(seq)):
        seq[i] = dic[seq[i]]
    print(*seq)