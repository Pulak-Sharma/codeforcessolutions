s = list(input())
remove = ['{', '}', ',']
s = [x for x in s if x not in remove and x != ' ']
print(len(set(s)))