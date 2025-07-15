func maxProfit(prices []int) int {
    result := 0
    maxPrice := prices[len(prices) - 1]
    for i:= len(prices) - 2; i > -1; i --{
        if maxPrice < prices[i]{
            maxPrice = prices[i]
        }
        if result < maxPrice - prices[i]{
            result = maxPrice - prices[i]
        }
    }
    return result
}