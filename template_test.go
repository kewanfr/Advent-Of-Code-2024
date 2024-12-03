package template

import (
	"fmt"
	"testing"
)

func TestPartOne(t *testing.T){
	t.Run("Part", func(t *testing.T) {
		// expected := 0
		actual := partone("input.txt")
		
		fmt.Println("Part One: ", actual)
		// if expected != actual{
		// 	t.Fail()
		// }
	})
}

func TestPartTwo(t *testing.T){
	t.Run("Part", func(t *testing.T) {
		// expected := 0
		actual := parttwo("input.txt")

		fmt.Println("Part Two: ", actual)
		
		// if expected != actual{
		// 	t.Fail()
		// }
	})
}