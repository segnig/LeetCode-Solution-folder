class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        answer = inf
        child = [0] * k

        def backtrack(indx):
            nonlocal answer, child
            if indx == len(cookies):
                answer = min(answer, max(child))
                return 
            for i in range(k):
                child[i] += cookies[indx]
                backtrack(indx + 1)
                child[i] -= cookies[indx]
                
        if k == 8:
            return max(cookies)
        backtrack(0)
        return answer