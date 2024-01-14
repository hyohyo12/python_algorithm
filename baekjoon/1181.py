#1181 / 단어 정렬
#문자열, 정렬
import sys
input = sys.stdin.readline
def StringSort(string):
    string.sort()
    string.sort(key = len)
    for i in string:
        print(i)
if __name__ == "__main__":
    string = []
    for i in range(int(input())):
        string.append(input().strip())
    string = set(string)
    string = list(string)
    StringSort(string)