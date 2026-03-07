'''
Find Missing Transaction ID
'''
class Solution:
    def solution(self, nums):
        n = len(nums)+1
        total = n*(n+1)//2
        current = sum(nums)

        return total - current