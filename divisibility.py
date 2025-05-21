t = int(input())
outputstr = []
for i in range(t):
    a,b = map(int, input().split())
    if a % b == 0:
        output = 0
    else:
        output = b - (a % b)
    outputstr.append(str(output))   
print('\n'.join(outputstr))
        