class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p=m+n-1
        p1=m-1
        p2=n-1
        while p2>=0 and p1>=0:
            if nums2[p2]>=nums1[p1]:
                nums1[p]=nums2[p2]
                p2-=1
            else:
                nums1[p]=nums1[p1]
                p1-=1
            p-=1
        if p1<0:
            while p2>=0:
                nums1[p]=nums2[p2]
                p2-=1
                p-=1