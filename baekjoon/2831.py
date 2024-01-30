import sys
import bisect
input = sys.stdin.readline

def find_pair(p_seq: list[int],n_seq: list[int])->int:
    start = 0
    global count
    end = len(p_seq)-1
    while start < len(n_seq) and end >= 0:
        if p_seq[end]+n_seq[start] < 0:
            count += 1
            end -= 1
            start += 1
        else:
            end -= 1

if __name__ == "__main__":
    n = int(input())
    b_seq = sorted(list(map(int,input().split())))
    g_seq = sorted(list(map(int,input().split())))
    count = 0
    b_positive_index = bisect.bisect_left(b_seq,0)
    g_positive_index = bisect.bisect_left(g_seq,0)
    
    find_pair(b_seq[b_positive_index:],g_seq[:g_positive_index])
    find_pair(g_seq[g_positive_index:],b_seq[:b_positive_index])
    
    print(count)