package main

import (
	"fmt"
)

type Stack struct {
	data []string
}

func (s *Stack) Push(item string) {
	s.data = append(s.data, item)
}

func (s *Stack) Pop() string {
	if len(s.data) == 0 {
		return ""
	}
	item := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return item
}

func (s *Stack) Top() string {
	if len(s.data) == 0 {
		return ""
	}
	return s.data[len(s.data)-1]
}

func (s *Stack) IsEmpty() bool {
	return len(s.data) == 0
}

func isOpen(ch string) bool {
	return ch == "{" || ch == "(" || ch == "["
}

func isPair(open, close string) bool {
	return (open == "{" && close == "}") ||
		(open == "[" && close == "]") ||
		(open == "(" && close == ")")
}

func isValid(s string) bool {
	stack := &Stack{}

	for i := 0; i < len(s); i++ {
		if isOpen(string(s[i])) {
			stack.Push(string(s[i]))
		} else {
			if !stack.IsEmpty() && isPair(stack.Top(), string(s[i])) {
				stack.Pop()
			} else {
				return false
			}
		}
	}

	return stack.IsEmpty()
}

func main() {
	str := "{[]}"
	fmt.Println(isValid(str)) // Output: true
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode = nil
	cur := head

	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev
}
