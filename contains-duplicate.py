class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True

obj=Solution()
print(obj.containsDuplicate([1,2,3,1]))