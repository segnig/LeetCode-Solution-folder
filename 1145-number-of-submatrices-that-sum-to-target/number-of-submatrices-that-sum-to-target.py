class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)+1
        m = len(matrix[0])+1

        prefix = [[0]*m for i in range(n)]

        for i in range(1,n):
            for j in range(1,m):
                prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+matrix[i-1][j-1]
        ans=0
        for r1 in range(n):
            for r2 in range(r1 + 1,n):
                stored = defaultdict(int)
                for col in range(m):
                    needs = prefix[r2][col]-prefix[r1][col]
                    ans+=stored[needs - target]
                    stored[needs]+=1
        return ans


                    