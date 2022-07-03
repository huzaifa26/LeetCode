# Actual Solution
class Solution(object):
    def pivotIndex(self, nums):
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        
        lsum=0
        rsum=s
        
        for i in range(len(nums)):
            rsum-=nums[i]
            if lsum==rsum:
                return i
            lsum+=nums[i]
        
        return -1


#My solution. Time Limit Exceeded(735 / 745 test cases passed.)
class Solution(object):
    def pivotIndex(self, nums):
        pivotIndex=-1
        leftsum=0

        for i in range(len(nums)):
            key=i+1
            rigthsum=0

            if i < key and i != 0:
                leftsum=leftsum+nums[i-1]

            index=key
            while index < len(nums):
                rigthsum=rigthsum+nums[index]
                index=index+1

            if leftsum == rigthsum:
                pivotIndex=i
                return pivotIndex  
        return -1      

ss= Solution()
r=ss.pivotIndex([-1,-1,0,0,-1,-1])
print(r)