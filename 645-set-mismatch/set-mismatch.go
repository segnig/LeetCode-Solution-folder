func findErrorNums(nums []int) []int {
    store := make(map[int]int)

    for i:= 0;i < len(nums); i++ {
        store[nums[i]] += 1
    }

    var result []int
    var missed []int

    for i:= 1;i < len(nums) + 1; i++ {
        if store[i] != 1{
            if store[i] == 0{
                missed = append(missed, i)
            }else{
                result = append(result, i)
            }
        }
    }
    result = append(result, missed...)
    return result
}