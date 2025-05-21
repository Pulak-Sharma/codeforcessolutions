n = int(input())
heights = list(map(int, input().split()))
max_index = heights.index(max(heights))
min_index = heights.index(min(heights))
if max_index>min_index:
    moves = max_index + (n - 1 - min_index) - 1
else:
    # Otherwise, no overlap
    moves = max_index + (n - 1 - min_index)
print(moves)


n = int(input())
heights = list(map(int, input().split()))

# Find the index of the tallest soldier (first occurrence)
max_index = heights.index(max(heights))

# Find the index of the shortest soldier (last occurrence)
min_index = len(heights) - 1 - heights[::-1].index(min(heights))

if max_index > min_index:
    moves = max_index + (n - 1 - min_index) - 1
else:
    moves = max_index + (n - 1 - min_index)
print(moves)