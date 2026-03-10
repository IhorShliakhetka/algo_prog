def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []

    m = len(matrix)
    n = len(matrix[0])
    result = []

    for d in range(m + n - 1):
        if d % 2 == 0:
            i = min(d, m - 1)
            j = d - i
            while i >= 0 and j < n:
                result.append(matrix[i][j])
                i -= 1
                j += 1
        else:
            j = min(d, n - 1)
            i = d - j
            while j >= 0 and i < m:
                result.append(matrix[i][j])
                i += 1
                j -= 1

    return result