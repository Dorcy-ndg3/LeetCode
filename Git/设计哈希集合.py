class MyHashSet(object):
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [0 for _ in range(1000005)]
 
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.list[key] = 1
        
 
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.list[key] = 0
        
 
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.list[key] == 1


        