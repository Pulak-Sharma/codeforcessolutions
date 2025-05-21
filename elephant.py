x = int(input())
steps = 0
for i in range(1,6):
    if x==i:
        steps = 1
        print(steps)
if x>5:
    if x%5==0:
        steps += int(x/5)
        print(steps)
    else:
        steps = int(x/5) + 1
        print(steps)