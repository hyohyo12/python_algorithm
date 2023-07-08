tc=int(input())
for i in range(tc):
    inString=input()
    if(len(inString)==1):
        print("{0}{1}".format(inString[0],inString[0]))
    else:
        print("{0}{1}".format(inString[0],inString[len(inString)-1]))