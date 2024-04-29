def longestValidSequence(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_length = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def isValid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def backtrack(x, y, prev, length, is_greater, visited):
        nonlocal max_length

        max_length = max(max_length, length)
        visited[x][y] = True

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if isValid(new_x, new_y) and not visited[new_x][new_y]:
                if is_greater:
                    if matrix[new_x][new_y] < prev:
                        backtrack(new_x, new_y, matrix[new_x][new_y], length + 1, not is_greater, visited)
                else:
                    if matrix[new_x][new_y] > prev:
                        backtrack(new_x, new_y, matrix[new_x][new_y], length + 1, not is_greater, visited)
        # 回溯前重置visited
        visited[x][y] = False

    for i in range(rows):
        for j in range(cols):
            visited = [[False] * cols for _ in range(rows)]
            backtrack(i, j, matrix[i][j], 1, True, visited)
            backtrack(i, j, matrix[i][j], 1, False, visited)

    return max_length

# 测试
matrix = [
    [2, 1, 3],
    [4, 2, 1],
    [3, 5, 5]
]
print(longestValidSequence(matrix))  # 输出应该为 5
