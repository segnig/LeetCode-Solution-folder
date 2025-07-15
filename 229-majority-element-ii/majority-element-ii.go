func majorityElement(nums []int) []int {
    var result []int

    numCounter := make(map[int]uint)

    for _, num := range nums{
        numCounter[num]++
    }
    for num, count := range numCounter{
        if float64(count) > float64(len(nums) / 3){
            result = append(result, num)
        }
    }
    return result 
}