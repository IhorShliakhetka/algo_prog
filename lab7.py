import csv


def matrix(file_path: str) -> list[list[int]]:
    result_matrix = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                result_matrix.append([int(x) for x in row])
    return result_matrix


def cable_length(matrix_data: list[list[int]]) -> int:
    if not matrix_data:
        return 0

    n = len(matrix_data)
    if n == 1:
        return 0

    visited = [False] * n
    min_weights = [float("inf")] * n
    min_weights[0] = 0
    total_length = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_weights[i] < min_weights[u]):
                u = i

        if min_weights[u] == float("inf"):
            raise ValueError("Неможливо з'єднати всі острови")

        visited[u] = True
        total_length += min_weights[u]

        for v in range(n):
            weight = matrix_data[u][v]
            if weight > 0 and not visited[v] and weight < min_weights[v]:
                min_weights[v] = weight

    return total_length


if __name__ == "__main__":
    island_matrix = matrix("islands.csv")
    result = cable_length(island_matrix)
    print(f"Мінімальна довжина підводних кабелів: {result}")