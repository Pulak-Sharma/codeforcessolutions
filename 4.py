for _ in range(int(input())):
    s = input()
found = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:  # Check for two consecutive identical characters
            print(s[i:i + 2])
            found = True
            break
    if not found:
        print(-1)
    