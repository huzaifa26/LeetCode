class Solution:
    def subsets(self, nums):
        arr=[]
        arr.append([])
        for i in range(len(nums)):
            # arr.append([nums[i]])
            for j in range(i+1,len(nums)):
                # arr.append([nums[i],nums[j]])

        
        return arr

ss=Solution()
print(ss.subsets([1,2,3]))