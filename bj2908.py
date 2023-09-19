firstNum,secondNum = input().split()
firstList = list(firstNum)
secondList = list(secondNum)
firstList.reverse()
secondList.reverse()
intFirst = [int(i) for i in firstList]
intSecond = [int(i) for i in secondList]
firstTmp=''.join(map(str,intFirst))
secondTmp=''.join(map(str,intSecond))
firstNo = int(firstTmp)
secondNo = int(secondTmp)
if(firstNo>secondNo):
    print(firstNo)
elif(firstNo<secondNo):
    print(secondNo)