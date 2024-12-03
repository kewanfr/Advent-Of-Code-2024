package dec1

import (
	"fmt"
	"testing"
)

func TestPartOne(t *testing.T){
	t.Run("Part", func(t *testing.T) {
		// expected := 0
		actual := partone("input.txt")
		
		fmt.Println(actual)
		// if expected != actual{
		// 	t.Fail()
		// }
	})
}

func TestPartTwo(t *testing.T){
	t.Run("Part", func(t *testing.T) {
		// expected := 0
		actual := parttwo("input.txt")
		fmt.Println(actual)
		
		// if expected != actual{
		// 	t.Fail()
		// }
	})
}