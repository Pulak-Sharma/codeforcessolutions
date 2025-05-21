i = 1
series = []
while len(series) < 1000:  # Generate enough numbers for any reasonable input
    if i % 3 != 0 and i % 10 != 3:
        series.append(i)
    i += 1
output = ''
for _ in range(int(input())):
    k = int(input())
    output+= str(series[k-1])+'\n'
print(output)
