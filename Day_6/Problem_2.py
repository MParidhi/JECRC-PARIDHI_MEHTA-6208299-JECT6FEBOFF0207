'''
Sum of Alternating Square Series
'''
class Solution:
    def sum_series(self, n):
        total = 0
        for i in range(1,n+1):
            sq=i**2

            if i<=2:
                total+=sq
            else:
                if i%2==0:
                    total+=sq
                else:
                    total-=sq
        return total