class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        if target not in nums:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
            else:
                return len(nums)
            
                    
            
        