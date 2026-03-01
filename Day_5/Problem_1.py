'''
Word Frequency Counter
'''
class Solution:
    def word_frequency(self, sentence):
        words = sentence.split()
        freq={}
        for i in words:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        return freq
     
       