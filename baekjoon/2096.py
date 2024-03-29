import sys
input = sys.stdin.readline



def main():
    n = int(input())
    seq = list(map(int,input().split()))
    dp_max = seq
    dp_min = seq
    for _ in range(n-1):
        seq = list(map(int,input().split()))
        dp_max = [seq[0]+max(dp_max[0],dp_max[1]),seq[1]+max(dp_max),seq[2]+max(dp_max[1],dp_max[2])]
        dp_min = [seq[0]+min(dp_min[0],dp_min[1]),seq[1]+min(dp_min),seq[2]+min(dp_min[1],dp_min[2])]
    print(max(dp_max),min(dp_min))
if __name__ =="__main__":
    main()