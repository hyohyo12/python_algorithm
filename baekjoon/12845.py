n = int(input())
cards = list(map(int,input().split()))
cards.sort(reverse=True)
gold = 0
maxLevel = cards[0]
for i in range(1,n):
    gold += maxLevel+cards[i]
print(gold)