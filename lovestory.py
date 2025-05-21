c = 'codeforces'
for _ in range(int(input())):
    output = 0
    s = input()
    for i in range(len(c)):
        if c[i]!=s[i]:
            output +=1
    print(output)