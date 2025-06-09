class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: (x[0], -(x[1] - x[0])))

        # track the cadidate 
        candidates = []
        used = []
        pointer = 0
        possible = True

        for i in range(len(nums)):
            while pointer < len(queries) and queries[pointer][0] == i:
                heappush(candidates, -queries[pointer][1])
                pointer += 1
            while used and used[0] < i:
                heappop(used)

            while candidates and nums[i] > len(used):
                right = - heappop(candidates)
                if right >= i:
                    heappush(used, right)
            
          
            if len(used) < nums[i]:
                possible = False
                break
        if possible:
            return len(candidates)
        else:
            return -1            

