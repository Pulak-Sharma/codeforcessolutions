for _ in range(int(input())):
    n = int(input())
    s = input()
    balloons = 0
    visited = set()
    for char in s:
        if char not in visited:
            balloons += 2  # First occurrence of the character
            visited.add(char)
        else:
            balloons += 1  # Subsequent occurrence of the character

    print(balloons)
