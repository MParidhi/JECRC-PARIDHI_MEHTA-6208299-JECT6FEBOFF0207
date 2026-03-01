'''
Shopping Discount System
'''
class Solution:
    def discount(self, total_amount, is_member):
        ## Write your code here & don't forget to use "return" keyword
        bill=0
        if total_amount>=5000:
            if is_member:
                bill=total_amount*0.80
            else:
                bill=total_amount*0.90
        else:
            if is_member:
                bill=total_amount*0.95
            else:
                bill=total_amount
        return bill
        