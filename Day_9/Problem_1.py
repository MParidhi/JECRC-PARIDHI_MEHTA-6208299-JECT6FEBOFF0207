'''
Circular Array Rotation Equilibrium
'''
class Solution:
    def count_equilibrium_rotations(self, arr):
        n = len(arr)
        count = 0

        for r in range(n):
            found=False

            for i in range(n):
                left_sum=0
                right_sum=0

                for j in range(i):
                    left_sum=left_sum + arr[(j-r) % n]
                
                for j in range(i+1, n):
                    right_sum=right_sum + arr[(j-r) % n]

                if left_sum == right_sum:
                    found = True
                    break
        
            if found:
                count = count+1

        return count
        