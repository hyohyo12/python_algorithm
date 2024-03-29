# import sys
# a=[]
# allBreak=True
# for i in range(9):
#     a.append(int(sys.stdin.readline()))
# sum_a = sum(a)
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if i == j:
#             continue
#         else:
#             if sum_a-(a[i]+a[j]) == 100:
#                 tmp = a[j]
#                 a.pop(i)
#                 a.remove(tmp)
#                 allBreak = False
#                 break
#     if allBreak == False:
#         break
# a.sort()
# for i in a:
#     print(i)


import sys
input = sys.stdin.readline

def main():
    seq = [int(input()) for _ in range(9)]
    seq.sort()
    tmp = sum(seq)
    left,right = 0,len(seq)-1
    while left < right:
        cur = tmp - (seq[left]+seq[right])
        if cur == 100:
            for i in range(len(seq)):
                if i == left or i == right:
                    continue
                print(seq[i])
            break
        elif cur < 100:
            right -= 1
        else:
            left += 1

if __name__ == "__main__":
    main()
    
