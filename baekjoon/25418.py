#25418 정수 a를 k로 만들기

def ans(a,k):
    count = 0
    while 1:
        if a == k:
            return count
        if k%2 == 0 and a*2 <= k:
            k = int(k//2)
        else:
            k-=1
        count += 1
if __name__ == "__main__":
    a,k = map(int,input().split())
    print(ans(a,k))