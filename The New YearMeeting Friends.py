positions = list(map(int, input().split()))
positions.sort()
distance = (positions[1] - positions[0]) + (positions[2] - positions[1])
print(distance)