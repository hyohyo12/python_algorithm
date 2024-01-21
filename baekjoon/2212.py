def min_dist(n:int,k:int,seq:list[int])->int:
    seq.sort()
    def get_dist():
        dist = []
        for i in range(1,n):
            dist.append(seq[i]-seq[i-1])
        dist.sort()
        return dist
    dist = get_dist()
    return sum(dist[:n-k])




if __name__ == "__main__":
    n = int(input())
    k = int(input())
    seq = list(map(int,input().split()))
    print(min_dist(n,k,seq))