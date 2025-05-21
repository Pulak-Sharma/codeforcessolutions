n = int(input())
output = ''
hate = 'I hate'
love = 'I love'
for i in range(1,n+1):
    if i%2==1:
        if i<n:
            output += hate + ' that '
        else:
            output += hate + ' it'
    else:
        if i<n:
            output += love + ' that '
        else:
            output += love + ' it'
print(output)