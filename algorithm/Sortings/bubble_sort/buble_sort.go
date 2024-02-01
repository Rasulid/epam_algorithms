package main

import "fmt"

func main() {
	arr := []int{1, 9, 5, 2, 5, 7, 31, 70}

	fmt.Println(DubbleSort(arr))
}

func DubbleSort(arr []int) []int {

	for i := 0; i < len(arr); i++ {

		isSorted := true

		for j := 1; j < len(arr)-i; j++ {

			if arr[j] < arr[j-1] {

				isSorted = false

				arr[j], arr[j-1] = arr[j-1], arr[j]

			}
		}
		if isSorted {
			break
		}
	}

	return arr
}
