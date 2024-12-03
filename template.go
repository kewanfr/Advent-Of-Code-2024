package template

import (
	"bufio"
	"fmt"
	"os"
)

func main() {


	fmt.Println(partone("input.txt"))
	fmt.Println(parttwo("input.txt"))
}

func partone(fileName string) (answer int) {

	file, _ := os.Open(fileName)

	scanner := bufio.NewScanner(file)
	var content string

	for scanner.Scan(){
		line := scanner.Text()
		content += line
		answer += 1
	}


	return answer
}
func parttwo(fileName string) (answer int) {

	file, _ := os.Open(fileName)

	scanner := bufio.NewScanner(file)
	var content string

	for scanner.Scan(){
		line := scanner.Text()
		content += line
		answer += 1
	}


	return answer
}