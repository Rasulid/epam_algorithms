def CountingSort(array: list) -> list:
    minimum = array[0]
    maximum = array[0]

    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
        if array[i] < minimum:
            minimum = array[i]

    vector = [0] * (maximum - minimum + 1)

    return vector


arr = [5, 11, 6, 3, 8, 10, 7, 7, 5, 6, 10, 15]
result = CountingSort(arr)
print(len(result))
