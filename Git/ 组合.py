class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools
 
        return list(itertools.combinations(range(1,n+1),k))


       