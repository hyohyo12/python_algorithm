s = input()
word = 'UCPC'
count = 0
for i in s:
    if i == word[count]:
        count+=1
    if count == 4:
        print("I love UCPC")
        break
else:
    print('I hate UCPC')