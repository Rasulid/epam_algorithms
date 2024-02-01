package main

import (
	"errors"
	"fmt"
)

type Queue struct {
	array []interface{}
}

func NewQueue() *Queue {
	return &Queue{array: []interface{}{}}
}

func (q *Queue) IsEmpty() bool {
	return len(q.array) == 0
}

func (q *Queue) Pop() (interface{}, error) {
	if q.IsEmpty() {
		return nil, errors.New("empty queue")
	}

	deletedItem := q.array[0]
	q.array = q.array[1:]
	return deletedItem, nil
}

func (q *Queue) Push(item interface{}) {
	q.array = append(q.array, item)
}

func (q *Queue) Top() interface{} {
	return q.array[0]
}

func (q *Queue) Size() int {
	return len(q.array)
}

func main() {
	queue := NewQueue()

	queue.Push(1)
	queue.Push(2)
	queue.Push(3)

	first := queue.Top()
	fmt.Println("First element of the queue:", first) // First element of the queue: 1

	fmt.Println("Size of the queue:", queue.Size()) // Size of the queue: 3

	item, _ := queue.Pop()
	fmt.Println("Dequeued element:", item) // Dequeued element: 1

	item, _ = queue.Pop()
	fmt.Println("Dequeued element:", item)                        // Dequeued element: 2
	fmt.Println("Size of the queue after dequeue:", queue.Size()) // Size of the queue after dequeue: 1

	first = queue.Top()

	fmt.Println("First element of the queue:", first)
}
