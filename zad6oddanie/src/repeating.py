def find_repeating_elements(numbers, size):
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    result = [n for n, c in counts.items() if c == size]
    return result
