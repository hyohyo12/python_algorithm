#1259 / 팰린드롬수
#구현,문자열

while True:
    n = int(input())
    if n == 0:
        break
    n = list(map(int,str(n)))
    if n == list(reversed(n)):
        print('yes')
    else:
        print('no')