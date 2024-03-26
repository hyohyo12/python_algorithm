import sys
input = sys.stdin.readline

def multi_tap_scheduling(seq:list[int],n:int,k:int):
    cnt = 0
    occupy = []
    for i in range(k):
        if seq[i] in occupy:
            continue
        
        if len(occupy) != n:
            occupy.append(seq[i])
            continue

        max_later = 0
        tmp = 0
        
        for plug in occupy:
            if plug not in seq[i:]:
                tmp = plug
                break
            
            elif max_later < seq[i:].index(plug):
                max_later = seq[i:].index(plug)
                tmp = plug
        occupy[occupy.index(tmp)] = seq[i]
        cnt += 1
        
    return cnt

    # q = []
    # cnt = 0
    # occupy = [0 for _ in range(101)]
    # freq_table = [0 for _ in range(101)]
    # for i in range(len(seq)):
    #     freq_table[seq[i]] += 1
    # for i in range(k):
    #     if len(q) < n:
    #         heapq.heappush(q,[freq_table[seq[i]],seq[i]])
    #         occupy[seq[i]] = 1
    #     else:
    #         if occupy[seq[i]]:
    #             for j in range(len(q)):
    #                 if q[j][1] == seq[i]:
    #                     q[j][0] -= 1
    #                     break
    #         else:
    #             freq,tmp = heapq.heappop(q)
    #             occupy[tmp] = 0
    #             heapq.heappush(q,[freq_table[seq[i]],seq[i]])
    #             freq_table[tmp] = freq-1
    #             cnt += 1
    # return cnt
    
def main():
    n,k = map(int,input().split())
    seq = list(map(int,input().split()))
    print(multi_tap_scheduling(seq,n,k))
    
if __name__ == "__main__":
    main()