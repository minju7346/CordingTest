class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ctr = Counter(nums1)
        res = []
        for n in nums2:
            if ctr[n]:
                res+=[n]
                ctr[n] -= 1
        return res