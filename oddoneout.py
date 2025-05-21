output = ''
for _ in range(int(input())):
    str = input()
    str = str.replace(" ", "")
    for char in str:
        if str.count(char)==1:
            output+=char+'\n'
print(output)
