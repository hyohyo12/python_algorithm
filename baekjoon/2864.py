a,b = input().split()
print('{0} {1}'.format(int(a.replace('6','5'))+int(b.replace('6','5')),int(a.replace('5','6'))+int(b.replace('5','6'))))