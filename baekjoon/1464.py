from collections import deque
def smart_reverse(seq: list[str]):
    q = deque(seq[0])
    for i in range(1,len(seq)):
        if seq[i] <= q[-1] and q[0] >= seq[i]:
            q.appendleft(seq[i])
        else:
            q.append(seq[i])
    return list(q)



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    str_seq = list(input().strip())
    print(''.join(smart_reverse(str_seq)))