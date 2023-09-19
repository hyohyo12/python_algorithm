alphabet = ['b','d','p','q','i','o','v','w','x']
def mirror(words):
    result=[]
    for i in range(len(words)-1,-1,-1):
        if words[i] in alphabet:
            if words[i] == 'd':
                result.append('b')
            elif words[i] == 'b':
                result.append('d')
            elif words[i] == 'q':
                result.append('p')
            elif words[i] == 'p':
                result.append('q')
            else:
                result.append(words[i])
        else:
            return "INVALID"      
    return ''.join(result)
if __name__ == '__main__':
    while True:
        words = input()
        if words == '#':
            break
        else:
            words = list(words)
            print(mirror(words))