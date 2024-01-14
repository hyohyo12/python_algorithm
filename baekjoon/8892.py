import sys
input = sys.stdin.readline

def find_palindrome(string:list[str])->str:
    for i in range(len(string)-1):
        for j in range(i+1,len(string)):
            tmp = string[i]+string[j]
            if tmp == tmp[::-1]:
                return tmp
            elif string[j]+string[i] == (string[j]+string[i])[::-1]:
                return string[j]+string[i]
    else:
        return 0
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        string = []
        for i in range(n):
            string.append(input().strip())
        print(find_palindrome(string))