class Solution(object):
    def maxCount(self, banned, m, maxSum):
        # Sort the banned list
        banned.sort()

        count = 0 
        result = 0 
        l = 1

        for n in banned:
            if n > m:
                break
            if n > maxSum:
                return count

            if n > l:
                range_sum = (n - l) * (l + n - 1) // 2
                print(range_sum)
                if result + range_sum > maxSum:
                    remaining = maxSum - result
                    
                    x = int((-1 * (2 * l - 1) + ((2 * l - 1) ** 2 + 8 * remaining) ** 0.5) // 2)
                    return count + max(0, x)

                result += range_sum
                count += n - l
            l = n + 1  

        if l <= m:
            
            range_sum = (m - l + 1) * (l + m) // 2
            print(range_sum)

            if result + range_sum > maxSum:
                remaining = maxSum - result
                x = int((-1 * (2 * l - 1) + ((2 * l - 1) ** 2 + 8 * remaining) ** 0.5) // 2)
                return count + max(0, x)  

            result += range_sum
            count += m - l + 1

        return count
