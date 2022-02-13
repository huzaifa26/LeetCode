class Solution:
    def subsets(self, nums):
        for i in range(len(nums)):
            arr=[]
            for j in range(i):
                print(nums[j])

ss=Solution()
ss.subsets([1,2,3])