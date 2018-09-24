# def mark_island(binary_matrix, i, j, row_count, col_count):
#     if i < 0 or i >= row_count - 1 or j < 0 or j >= col_count - 1:
#         return
#     else:
#         if binary_matrix[i - 1][j] == 1:
#             binary_matrix[i - 1][j] = -1  # visited
#             mark_island(binary_matrix, i - 1, j, row_count, col_count)
#         elif binary_matrix[i + 1][j] == 1:
#             binary_matrix[i - 1][j] = -1  # visited
#             mark_island(binary_matrix, i + 1, j, row_count, col_count)
#         elif binary_matrix[i][j - 1] == 1:
#             binary_matrix[i][j - 1] = -1  # visited
#             mark_island(binary_matrix, i, j - 1, row_count, col_count)
#         elif binary_matrix[i][j + 1] == 1:
#             binary_matrix[i][j + 1] = -1  # visited
#             mark_island(binary_matrix, i, j + 1, row_count, col_count)


def dfs(binary_matrix, i, j):
    if i < 0 or i >= len(binary_matrix) or j < 0 or j >= len(binary_matrix[0]):
        return

    if binary_matrix[i][j] == 1:
        binary_matrix[i][j] = -1
        dfs(binary_matrix, i - 1, j)
        dfs(binary_matrix, i + 1, j)
        dfs(binary_matrix, i, j - 1)
        dfs(binary_matrix, i, j + 1)


def get_number_of_islands(binary_matrix):
    if binary_matrix is None or len(binary_matrix) < 1 or len(binary_matrix[
                                                                  0]) < 1:
        return 0

    row_count = len(binary_matrix)
    col_count = len(binary_matrix[0])

    if row_count == 0 and col_count == 0:
        return binary_matrix[row_count][col_count]

    island_count = 0

    for i in range(0, row_count):
        for j in range(0, col_count):
            if binary_matrix[i][j] == 1:
                dfs(binary_matrix, i, j)
                island_count += 1

    return island_count


binaryMatrix = [[1, 0, 1, 0],
                [0, 1, 1, 1],
                [0, 0, 1, 0]]
# binaryMatrix = [[1, 0, 1, 0]]
print(get_number_of_islands(binaryMatrix))
