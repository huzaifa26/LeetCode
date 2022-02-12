class Solution:
    def twoSum(self, nums, target):
        length=len(nums)
        self.answer=[]
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]+nums[j] ==  target:
                    self.answer.append(i)
                    self.answer.append(j)
                    return self.answer
            
sum=Solution()
s=sum.twoSum([2,7,11,15],9)
print(s)