import sys
input = sys.stdin.readline

class union_find:
    def __init__(self,size:int):
        self.root = [i for i in range(size+1)]
        self.rank = [1] * (size+1)
        
    
    def find(self,x:int):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.root[y_root] = x_root

            elif self.rank[x_root] < self.rank[y_root]:
                self.root[x_root] = y_root

            else:
                self.root[y_root] = x_root
                self.rank[x_root] += 1
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)


def main():
    n = int(input())
    m = int(input())
    uf = union_find(n)

    for i in range(1,n+1):
        tmp = list(map(int,input().split()))
        for idx,d in enumerate(tmp):
            if d:
                uf.union(i,idx+1)
    route = list(map(int,input().split()))
    
    for i in range(m-1):
        if not uf.is_connected(route[i],route[i+1]):
            print("NO")
            return
    print("YES")
    return
if __name__ == "__main__":
    main()