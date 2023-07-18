class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i,j=0,1
        maxdiff=0
        while j<len(nums):
            if i<j and nums[i]<nums[j]:
                diff=nums[j]-nums[i]
                maxdiff= max(diff,maxdiff)
            else:
                i=j
            j+=1
        

        return maxdiff if maxdiff else -1