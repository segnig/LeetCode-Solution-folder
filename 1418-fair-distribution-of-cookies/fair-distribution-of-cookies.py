class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        answer = inf
        child = [0] * k

        def backtrack(indx, max_so_far):
            nonlocal answer, child
            if indx == len(cookies):
                answer = min(answer, max_so_far)
                return 
            for i in range(k):
                child[i] += cookies[indx]
                backtrack(indx + 1, max(max_so_far, child[i]))
                child[i] -= cookies[indx]

                if child[i] == 0:
                    break


        if k == len(cookies):
            return max(cookies)
        backtrack(0, 0)
        return answer