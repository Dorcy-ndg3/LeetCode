class Solution(object):
    def plusOne(self, digits):
        for i in range(0,len(digits))[::-1]:
            digits[i]+=1
            digits[i]%=10
            if digits[i]!=0:
                return digits
        digits[0]=1
        digits.append(0)
        return digits