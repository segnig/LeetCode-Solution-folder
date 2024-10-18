class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        wor_df1 = defaultdict(int)
        wor_df2 = defaultdict(int)

        for i in range(len(word1)):
            wor_df1[word1[i]] += 1
            wor_df2[word2[i]] += 1
        print(wor_df1, wor_df2)
        for k in wor_df1:
            if abs(wor_df1[k] - wor_df2[k]) >= 4:
                return False
            print(abs(wor_df1[k] - wor_df1[k]))

        for k in wor_df2:
            if abs(wor_df1[k] - wor_df2[k]) >= 4:
                return False
            print(abs(wor_df1[k] - wor_df1[k]))

        return True



        