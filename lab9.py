def build_transition_table(needle):
    m = len(needle)
    unique_chars = set(needle)
    transition_table = [{char: 0 for char in unique_chars} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in unique_chars:
            if state < m and char == needle[state]:
                transition_table[state][char] = state + 1
            else:
                temp_str = needle[:state] + char
                for next_state in range(state, 0, -1):
                    if temp_str.endswith(needle[:next_state]):
                        transition_table[state][char] = next_state
                        break

    return transition_table


def finite_automaton_search(haystack, needle):
    if not needle:
        return []

    m = len(needle)
    n = len(haystack)
    transition_table = build_transition_table(needle)

    state = 0
    indices = []

    for i in range(n):
        char = haystack[i]
        state = transition_table[state].get(char, 0)

        if state == m:
            indices.append(i - m + 1)

    return indices