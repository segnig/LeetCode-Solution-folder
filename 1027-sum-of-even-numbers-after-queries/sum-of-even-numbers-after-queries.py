class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        # sum of the even nums
        is_even = lambda x: x % 2 == 0

        even_nums = filter(is_even, nums)

        sum_of_even_nums = sum(even_nums)

        result = []

        for val, index in queries:

            if nums[index] % 2 == 0:

                if (nums[index] + val) % 2 == 0:

                    sum_of_even_nums += val
                    nums[index] += val

                else:
                    sum_of_even_nums -= nums[index]
                    nums[index] += val

            else:
                if (nums[index] + val) % 2 == 0:
                
                    nums[index] += val
                    sum_of_even_nums += nums[index]
                    
                else:
                    nums[index] += val
            
            result.append(sum_of_even_nums)


        return result