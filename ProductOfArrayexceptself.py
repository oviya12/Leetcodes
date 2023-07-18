class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       

        i, j = 1, 1
        res=[1] * len(nums)
        for cur in range(len(nums)):
            res[cur] *= i
            res[-1-cur] *= j
            i *= nums[cur]
            j *= nums[-1-cur]
        return res
