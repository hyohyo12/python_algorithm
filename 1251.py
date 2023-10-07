import sys
input = sys.stdin.readline
string = list(input().strip())
ans = []
for i in range(1,len(string)-1):
    for j in range(i+1,len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ans.append(''.join(a+b+c))   
print(min(ans))