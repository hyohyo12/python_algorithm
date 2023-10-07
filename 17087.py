# 숨바꼭질 6
import sys
input = sys.stdin.readline
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def getDistance(peoples,s):
    distance = []
    for people in peoples:
        distance.append(abs(s-people))
    return distance.sort()
if __name__ == '__main__':
    n,s = map(int,input().split())
    bros = list(map(int,input().split()))
    distance = getDistance(bros,s)
    ans = distance[0]
    for i in range(1,n):
        ans = gcd(ans,distance[i])
    print(ans)

