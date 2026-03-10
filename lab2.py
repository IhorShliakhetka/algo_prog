def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        n = len(arr)
        
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(n):
            arr[i] = output[i]

        exp *= 10

    return arr


def max_hamsters(S, C, hamsters):
    left, right = 0, C
    answer = 0

    while left <= right:
        k = (left + right) // 2
        
        if k == 0:
            left = 1
            continue

        costs = []
        for H, G in hamsters:
            costs.append(H + G * (k - 1))

        radix_sort(costs)

        total = sum(costs[:k])

        if total <= S:
            answer = k
            left = k + 1
        else:
            right = k - 1

    return answer