'''
Maximum Alternating Subarray Score
'''
class Solution:
    def max_alternating_score(self, arr):
        n = len(arr)
        max_score = -10**9

        for i in range(n):
            score=0
            sign=1

            for j in range(i, n):
                score=score+sign*arr[j]
                sign=-sign

                if score>max_score:
                    max_score=score
        return max_score 