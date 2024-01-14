import sys
input = sys.stdin.readline

def ans(dna,m):
    distance = 0
    ans = ""
    for i in range(m):
        a,c,g,t = 0,0,0,0
        for j in range(len(dna)):
            if dna[j][i] == 'A':
                a+=1
            elif dna[j][i] == 'C':
                c+=1
            elif dna[j][i] == 'G':
                g+=1
            elif dna[j][i] == 'T':
                t+=1
        max_c = max(a,c,g,t)
        if max_c == a:
            ans+='A'
            distance += (c+g+t)
        elif max_c == c:
            ans+='C'
            distance+=(a+g+t)
        elif max_c == g:
            ans+='G'
            distance+=(a+c+t)
        elif max_c == t:
            ans+='T'
            distance+=(a+c+g)
    print(ans)
    print(distance)

if __name__ == "__main__":
    n,m = map(int,input().split())
    dna = []
    for i in range(n):
        dna.append(input().strip())
    ans(dna,m)