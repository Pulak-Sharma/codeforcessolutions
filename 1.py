for _ in range(int(input())):
    p = input()
    s = input()
    i, j = 0, 0
    while i < len(p) and j < len(s):
        if p[i] == s[j]:
            j += 1
        elif j + 1 < len(s) and s[j] == s[j + 1]:
            j += 1
        else:
            print("NO")
            break
        i += 1
    else:
        if i == len(p) and j == len(s):
            print("YES")
        else:
            print("NO")
