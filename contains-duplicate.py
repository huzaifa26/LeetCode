import time
start_time = time.time()

class Solution:
    def containsDuplicate(self, nums):
        obj={}
        for i in range(len(nums)):
            if obj.keys().__contains__(nums[i]):
                return nums[i]
            else:
                obj[nums[i]]=1
        return False

obj1=Solution()
print(obj1.containsDuplicate([0,4,5,0,3,6]))