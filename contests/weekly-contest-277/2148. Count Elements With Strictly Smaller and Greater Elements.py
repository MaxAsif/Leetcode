class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        # sort the num
        nums.sort()
        i = 1
        j = len(nums)-2
        while i < len(nums) and nums[i] == nums[i-1]:
            i+=1
        while j >= 0 and nums[j] == nums[j+1]:
            j-=1
        return max(0,j-i+1)