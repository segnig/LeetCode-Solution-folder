func separateDigits(nums []int) []int {
    var result []int

    for _, num := range nums{
        digits := toDigits(num)
        for i:= len(digits) - 1; i > -1; i--{
            result = append(result, digits[i])
        }
    }
    return result
    
}

func toDigits(num int) []int{
    var result []int

    for num > 0 {
        result = append(result, num % 10)
        num = int(num / 10)
    }
    return result
}