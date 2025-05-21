guest = input()
host = input()
pile = input()
if sorted(guest+host)==sorted(pile):
    print("YES")
else:
    print("NO")