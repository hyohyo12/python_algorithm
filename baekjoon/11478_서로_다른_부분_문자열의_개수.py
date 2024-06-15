import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    temp = set()
    for i in range(len(s)):
        for j in range(i,len(s)):
            temp.add(s[i:j+1])
    print(len(temp))


if __name__ == "__main__":
    main()