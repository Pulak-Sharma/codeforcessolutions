n = int(input())
levels = 0
cubes_used = 0
current_level = 1

while cubes_used + current_level <= n:
    cubes_used += current_level
    levels += 1
    current_level += levels + 1

print(levels)