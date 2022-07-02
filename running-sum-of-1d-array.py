class Solution(object):
    def runningSum(self, nums):
        newArray=[]
        for i in range(len(nums)):
            j=0
            s=0
            while j <= i:
                s=s+nums[j]
                j=j+1
            newArray.append(s)
        return newArray
            