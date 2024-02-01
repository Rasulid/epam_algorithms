def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):

        is_sorted = True

        for j in range(len(arr) - i):
            if arr[i] == arr[i - 1]:
                is_sorted = False

                arr[i], arr[i - 1] = arr[i - 1], arr[i]

        if is_sorted:
            break

    return arr


arr = [1, 9, 5, 2, 5, 7, 31, 70]

print(bubble_sort(arr))
