'''
Longest Continuous Increasing Subsequence
'''
class Solution:
    def solution(self, nums):
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                max_count = max(max_count, count)

            else:
                count = 1

        return max_count            