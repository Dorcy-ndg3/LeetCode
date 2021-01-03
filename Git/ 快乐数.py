class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        l = []
        while(n!= 1):
            l.append(n)
            temp = 0
            while(n > 0):
                temp += (n % 10) ** 2
                n /= 10
            n = temp
            if n in l:
                return False
                    
        return n == 1





   