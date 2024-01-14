from collections import deque
cards = deque(i+1 for i in range(int(input())))
while len(cards) != 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)
print(cards[0])