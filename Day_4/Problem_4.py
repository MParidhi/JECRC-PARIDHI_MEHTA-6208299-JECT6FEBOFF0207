'''
Bank EMI Payment Tracker
'''
class Solution:

    def calculate_total_paid(self, months):
        ## write your code here
        total_amnt=0
        curr_month=1
        if months<=0:
            return 'Invalid Duration'
        else:
            while curr_month<=months:
                total_amnt+=5000
                if total_amnt>50000:
                    total_amnt=50000
                    break
                curr_month+=1
        return total_amnt