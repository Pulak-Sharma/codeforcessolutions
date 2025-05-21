n = int(input())
cards = list(map(int, input().split()))
s = 0
d = 0
while True:
    if n==0:
        break
    s += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
    d += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
    n-=2
print(s,d)