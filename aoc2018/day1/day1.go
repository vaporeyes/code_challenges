package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	sum := 0
	file, err := os.Open("day1_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if i, err := strconv.Atoi(scanner.Text()); err == nil {
			sum += i
		}
	}
	fmt.Printf("sum = %d\n", sum)
	
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
