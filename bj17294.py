a=list(map(int,input()))
result = True
b=0
if(len(a)>=3):
    b=a[0]-a[1]
    for i in range(1,len(a)-1):
        if a[i]-a[i+1] != b:
            result=False
            break
print('''◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!''' if result else '''흥칫뿡!! <(￣ ﹌ ￣)>''')