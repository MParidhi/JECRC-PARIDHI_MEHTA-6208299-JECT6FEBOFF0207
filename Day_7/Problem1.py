'''
Hospital Bed Allocation Optimization
'''
class Solution:

    def solution(self, intervals):
        n = len(intervals)
        arrival = []
        discharge = []

        for i in intervals:
            arrival.append(i[0])
            discharge.append(i[1])

        beds = 1
        max_count = 1

        i = 1
        j = 0

        while i<n and j<n:
            if arrival[i] < discharge[j]:
                beds += 1
                max_count = max(max_count, beds)
                i+= 1

            else:
                beds -= 1
                j += 1

        return max_count               