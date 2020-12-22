class Solution(object):
    def lengthOfLastWord(self, s):
        end=len(s)
        while end>0 and s[end-1]==" ":
            end-=1
        if end==0:
            return 0
        start=end
        while start>0 and s[start-1]!=" ":
            start-=1
        return end-start