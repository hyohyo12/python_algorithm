import sys
input = sys.stdin.readline

member = []
for i in range(int(input())):
    age, name = input().strip().split()
    age = int(age)
    member.append((age,name))
member = sorted(member,key=lambda x:x[0])
for i in member:
    print(i[0], i[1])