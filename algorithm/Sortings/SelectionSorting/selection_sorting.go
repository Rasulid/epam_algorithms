package main

import "fmt"

func main() {
	arr := []int{15, 4, 3, 2, 7, 5, 6, 0, 8, 1}

	fmt.Println(SelectionSorting(arr))
}

func SelectionSorting(arr []int) []int {
	for j := 0; j < len(arr); j++ {
		minIndex := j

		for i := j + 1; i < len(arr); i++ {
			if arr[minIndex] > arr[i] {
				minIndex = i
			}
		}

		arr[j], arr[minIndex] = arr[minIndex], arr[j]
	}

	return arr
}

func smallerNumbersThanCurrent(nums []int) []int {
	var res []int

	for i := 0; i < len(nums); i++ {
		bNum := 0
		for j := 0; j < len(nums); j++ {
			if nums[j] < nums[i] && j != i {
				bNum++
			}
		}
		res = append(res, bNum)
	}
	return res
}
