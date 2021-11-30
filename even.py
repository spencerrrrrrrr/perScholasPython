def even(start, size):
    arr = []

    while (len(arr) < size):
        if start%2 == 0:
            arr.append(start)

        start += 1
    return arr

print(even(5, 7))