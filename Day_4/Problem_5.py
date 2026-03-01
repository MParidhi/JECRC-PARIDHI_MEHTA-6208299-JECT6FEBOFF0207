'''
Password Strength Checker
'''
class Solution:

    def check_password_strength(self, password):
        ## Write your solution here
        digits=0
        for i in password:
            if i in '0123456789':
                digits+=1
        if digits>=1:
            return 'Strong Password'
        elif len(password)<6:
            return 'Weak Password'
        else:
            return 'Moderate Password'