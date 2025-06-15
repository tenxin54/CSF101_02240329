class Solution:
    def twoSum(self, nums, target):
        for i in range (1, len(nums)):
           for j in range (1, len(nums)):
               if nums[j] + nums[j-i]==target:
                   return [j, j-i]
        return[]
    twoSum(self, nums, target)