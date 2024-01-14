def Rot13 (words):
    words = list(words)
    result = []
    tmp = 0
    for i in words:
        tmp = ord(i)
        if(65<=tmp and tmp<=90):#대문자일 경우
            if(tmp >= 78):#13을 더했을 때 오바되는 경우
                tmp = 64+(13-(90-tmp))
                result.append(chr(tmp))
            else:
                
                result.append(chr(tmp+13))
        elif(97<=tmp and tmp<=122): #소문자일 경우
            if(tmp >= 110):#13을 더했을 때 오바되는 경우
                tmp = 96+(13-(122-tmp))
                result.append(chr(tmp))
            else:
                result.append(chr(tmp+13))
        else:#공백이나 숫자일 경우
            result.append(chr(tmp))
    return ''.join(result)

if __name__ == "__main__":
    words = input()
    print(Rot13(words))