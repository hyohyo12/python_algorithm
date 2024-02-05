# def binary_serch(a_num:int,b_seq:list[int],bn:int)->bool:
#     left,right = 0,bn-1
#     while left <= right:
#         mid = (left+right)//2
#         if b_seq[mid] == a_num:
#             return False
#         elif b_seq[mid] > a_num:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return True

# if __name__ == "__main__":
#     an,bn = map(int,input().split())
    
#     a_seq = list(map(int,input().split()))
#     b_seq = sorted(list(map(int,input().split())))
    
#     ans = []
#     count = 0
#     for num in a_seq:
#         if binary_serch(num,b_seq,bn):
#             ans.append(num)
#             count += 1
#     print(count)
#     if count > 0: print(*sorted(ans))


an,bn = map(int,input().split())

a_seq = set(map(int,input().split()))
b_seq = set(map(int,input().split()))

a_seq -= b_seq

print(len(a_seq))
if len(a_seq) > 0:
    a_seq = sorted(list(a_seq))
    print(*a_seq)


