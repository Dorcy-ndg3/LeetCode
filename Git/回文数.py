def isPalindrome(self,x):
    """
    :type x: int
    :rtype: bool
    """

    x = str(x)
    num = x[::-1]
    if num == x:
        return True
    else:
        return False