func applyOperations(nums []int) []int {

    var result []int

    index := 0

    for index < len(nums) {
        if (index < len(nums) - 1) && nums[index] == nums[index + 1] {
            if nums[index] * 2 != 0{
                result = append(result, nums[index] * 2)
            }
            index += 2
        } else {
            if nums[index] != 0{
                result = append(result, nums[index])
            }
            index += 1
        }
    }

    for len(result) < len(nums){
        result = append(result, 0)
    }
    
    return result
}