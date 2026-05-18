def solve_ijones(w, h, grid):
    if w == 0 or h == 0:
        return 0

    letter_sum = {chr(i): 0 for i in range(97, 123)}

    paths = [1] * h

    for y in range(h):
        char = grid[y][0]
        letter_sum[char] += 1

    for x in range(1, w):
        new_paths = [0] * h

        for y in range(h):
            char = grid[y][x]

            new_paths[y] = letter_sum[char]

            prev_char = grid[y][x - 1]
            if prev_char != char:
                new_paths[y] += paths[y]

        for y in range(h):
            char = grid[y][x]
            letter_sum[char] += new_paths[y]
            paths[y] = new_paths[y]

    if h == 1:
        return paths[0]
    else:
        return paths[0] + paths[h - 1]


def main():
    with open("ijones.in", "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        if not first_line:
            return
        w, h = map(int, first_line.split())
        grid = [f.readline().strip() for _ in range(h)]

    result = solve_ijones(w, h, grid)

    with open("ijones.out", "w", encoding="utf-8") as f:
        f.write(str(result) + "\n")


if __name__ == "__main__":
    main()