package main

import "fmt"

func main() {

	arr := []int{1, 9, 3, 4, 0}

	fmt.Println(InsertionSort(arr))

}

func InsertionSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {

		currentNumb := arr[i]
		j := i - 1

		for j >= 0 && arr[j] > currentNumb {
			arr[j+1] = arr[j]
			j -= 1
		}

		arr[j+1] = currentNumb
	}

	return arr
}
