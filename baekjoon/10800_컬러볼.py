import sys
input = sys.stdin.readline

def main():
    n = int(input())
    color_table = [0 for _ in range(n+1)]
    seq = [(0,0,0)]
    res = [0]*(n+1)
    sum_seq = [0] * (n+1)
    for i in range(1,n+1):
        c,s = map(int,input().split())
        seq.append((c,s,i))
    seq.sort(key= lambda x:(x[1],x[0]))
    prev = 0
    tmp = 0
    for i in range(1,n+1):
        c,s,idx = seq[i]
        sum_seq[i] = sum_seq[i-1] + seq[i-1][1]
        if s == seq[i-1][1]:
            if c == seq[i-1][0]:
                res[idx] = max(0,prev - color_table[c]+(tmp*s))
                tmp += 1
            else:
                tmp = 1
                res[idx] = max(0,prev - color_table[c])
        else:
            tmp = 1
            res[idx] = max(0,sum_seq[i] - color_table[c])
            prev = sum_seq[i]
        color_table[c] += s
    for n in res[1:]:
        print(n)

if __name__ == "__main__":
    main()