n1 = input()
n2 = input()
n = ''
for i in range(len(n1)):
    if n1[i]==n2[i]:
        n += '0'
    else:
        n += '1'
print(n)