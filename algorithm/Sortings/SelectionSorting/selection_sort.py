from typing import List


def selection_Sort(arr: list):
    for j in range(len(arr)):
        min_ind = j
        for i in range(j + 1, len(arr)):  # Исправление: изменен диапазон внутреннего цикла
            if arr[min_ind] > arr[i]:
                min_ind = i

        arr[j], arr[min_ind] = arr[min_ind], arr[j]

    return arr


# arr = [1, 4, 0, 6, 3, 9, 2]
# print(selection_Sort(arr))

def smallerNumbersThanCurrent(nums: List[int]):
    res = []

    for i in range(len(nums)):
        b_num = 0
        for j in range(len(nums)):

            if nums[i] > nums[j] and j != i:
                b_num += 1
        res.append(b_num)

    return res


arr = [1, 4, 0, 6, 3, 9, 2]
print(smallerNumbersThanCurrent(arr))
