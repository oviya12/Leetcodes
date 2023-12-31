class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        mid=(i+j)//2
        
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
                
            elif target < nums[mid]:
                j=mid-1
                
            elif target>nums[mid]:
                i=mid+1
        return -1
                