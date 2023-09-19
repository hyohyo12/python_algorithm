count=0
b=['a','e','i','o','u','A','E','I','O','U']
while True:
    sentence=input()
    if sentence == '#':
        break;
    else:
        for i in sentence:
            if i in b:
                count+=1
        print(count)
        count=0