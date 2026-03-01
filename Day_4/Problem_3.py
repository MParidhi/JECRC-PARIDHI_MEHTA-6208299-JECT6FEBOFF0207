'''
Factory Production Defect Analyzer
'''
class Solution:

    def count_defective_products(self, total_products):
        ## Write your code here
        defective_cnt=0
        if total_products<=0:
            return 'Invalid Production Count'
        else:
            defective_cnt=total_products//5
            return defective_cnt