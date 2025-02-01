class Solution(object):
    def findOriginalArray(self, changed):
        changed.sort()

        hash_map = defaultdict(int)

        for num in changed:
            hash_map[num] += 1

        result = []
        
        for num in changed:
            if num in hash_map and num * 2 in hash_map:
                if num == 0:
                    if hash_map[num] > 1:
                        result.append(num)
                else:
                    result.append(num)

                hash_map[num*2] -= 1
                hash_map[num] -= 1

            if hash_map[num] <= 0:
                del hash_map[num]
            
            if hash_map[num * 2] == 0:
                del hash_map[num * 2]
        
        return [] if len(result) < len(changed) // 2 or len(changed) % 2 == 1 else result