nums = list(map(int,input().split()))
if nums == list(sorted(nums)):
    print("ascending")
elif list(sorted(nums)) == nums[::-1]:
    print("descending")
else:
    print("mixed")