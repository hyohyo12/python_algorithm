import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    
    result = []
    tmp = ''
    flag = 1
    for i in range(len(s)):
        if s[i] == "<":
            flag = 0
            if len(tmp) >= 1:
                result.append(tmp[::-1])
                tmp = ""
        elif s[i] == ">" :
            flag = 1
            tmp += ">"
            result.append(tmp)
            tmp = ""
            continue
        elif s[i] == " " and flag:
            result.append(tmp[::-1]+" ")
            tmp = ""
            continue
        elif i == len(s)-1 and len(tmp) >= 1:
            tmp += s[i]
            result.append(tmp[::-1])
            continue
        tmp += s[i]
    for r in result:
        print(r,end="")


if __name__ == "__main__":
    main()