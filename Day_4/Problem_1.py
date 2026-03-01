'''
ATM Withdrawal Simulation
'''
class Solution:

    def atm_withdrawal(self, pins, amount):
        balance = 10000
        correct_pin = 1234
        attempts = 0
        # Write your code here
        for p in pins:
            if p==correct_pin:
                if amount<=balance:
                    balance=balance-amount
                    return balance
                else:
                    return balance
            else:
                attempts+=1
                if attempts==3:
                    return "Block Account"
        
        return 'Account Blocked'