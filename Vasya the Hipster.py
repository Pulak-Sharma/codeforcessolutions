a,b = map(int, input().split())
different = min(a,b)
a -= different
b -= different
same = (a // 2) + (b // 2)
print(different,same)