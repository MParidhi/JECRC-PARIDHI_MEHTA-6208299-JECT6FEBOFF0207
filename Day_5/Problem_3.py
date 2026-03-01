'''
Remove Duplicate Transactions
'''
class Solution:
    def remove_duplicates(self, transactions):
        ## Write your code here & don't forget to use "return" keyword.
        unique_trans=[]
        for i in range(len(transactions)):
            duplicate=False
            for j in range(len(unique_trans)):
                if transactions[i]==unique_trans[j]:
                    duplicate=True
                    break
            if not duplicate:
                unique_trans.append(transactions[i])
        return unique_trans