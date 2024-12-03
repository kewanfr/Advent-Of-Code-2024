package dec1

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {


	fmt.Println(partone("input.txt"))
	fmt.Println(parttwo("input.txt"))
}

func partone(fileName string) (answer int) {

	file, _ := os.Open(fileName)

	scanner := bufio.NewScanner(file)
	var left []int
	var right []int

	for scanner.Scan(){
		line := scanner.Text()

		vals := strings.Split(line, "   ")

		val1, _ := strconv.Atoi(vals[0])
		val2, _ := strconv.Atoi(vals[1])
		
		left = append(left, val1)
		right = append(right, val2)
	}

	sort.Sort(sort.IntSlice(left))
	sort.Sort(sort.IntSlice(right))

	for i, _ := range left {

		if i < len(right){
			if right[i] > left[i] {
				answer += int(right[i]) - int(left[i])
			} else {
				answer += int(left[i]) - int(right[i])
			}
		}
	}

	return answer
}

func parttwo(fileName string) (answer int) {

	file, _ := os.Open(fileName)

	scanner := bufio.NewScanner(file)
	var left []int
	var right []int

	for scanner.Scan(){
		line := scanner.Text()

		vals := strings.Split(line, "   ")
		val1, _ := strconv.Atoi(vals[0])
		val2, _ := strconv.Atoi(vals[1])
		
		left = append(left, val1)
		right = append(right, val2)
	}

	sort.Sort(sort.IntSlice(left))
	sort.Sort(sort.IntSlice(right))

	for _, v := range left {

		count := 0

		for j := 0; j < len(right); j ++ {
			if right[j] == v {
				count ++
			}
		}

		answer += count*v
	}

	return answer
}