class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        thisset=set()
        for ele in nums:
            if ele not in thisset:
               thisset.add(ele)
            else:
                return True
        return False