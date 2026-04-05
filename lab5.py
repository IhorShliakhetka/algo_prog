def flood_fill(matrix, start_row, start_col, new_color):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    if start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols:
        raise IndexError("Початкові координати знаходяться поза межами матриці.")

    target_color = matrix[start_row][start_col]

    if target_color == new_color:
        return matrix

    stack = [(start_row, start_col)]

    while stack:
        r, c = stack.pop()

        if matrix[r][c] == target_color:
            matrix[r][c] = new_color

            if r > 0:
                stack.append((r - 1, c))
            if r < rows - 1:
                stack.append((r + 1, c))
            if c > 0:
                stack.append((r, c - 1))
            if c < cols - 1:
                stack.append((r, c + 1))

    return matrix


def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if len(lines) < 4:
        print("Недостатньо даних у файлі.")
        return
    try:
        height, width = map(int, lines[0].split(","))
        start_row, start_col = map(int, lines[1].split(","))

        new_color = lines[2].replace("'", "").replace('"', "").replace("‘", "").replace("’", "")

        matrix = []
        for line in lines[3:]:
            clean_line = line.rstrip(",")
            row = eval(clean_line)
            matrix.append(row)

    except Exception as e:
        print(f"Помилка парсингу вхідного файлу: {e}")
        return

    result_matrix = flood_fill(matrix, start_row, start_col, new_color)

    with open(output_file, "w", encoding="utf-8") as f:
        for i, row in enumerate(result_matrix):
            f.write(str(row))
            if i < len(result_matrix) - 1:
                f.write("\n")


if __name__ == "__main__":
    process_file("input.txt", "output.txt")
    print("Обробка завершена. Перевірте файл output.txt")