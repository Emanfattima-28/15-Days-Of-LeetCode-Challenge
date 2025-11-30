class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()          
        return len(s.split()[-1])
        