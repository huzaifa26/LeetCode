# class Solution:
#     def subarraySum(self, nums, k):
#         counter=0
#         for i in range(len(nums)):
#             summ=0
#             for j in range(i,len(nums)):
#                 print(nums[j])
#                 summ=summ+nums[j]
#                 if summ==k:
#                     counter=counter+1
#         return(counter)   
#
class Solution:
    def subarraySum(self, nums, k):
        counter=0
        summ=0
        j=0

        for j in range(len(nums)):
            summ=summ+nums[j]

            if summ==k:
                counter=counter+1
            print(summ==k)
            
            j=j+1
            if j <= len(nums):
                break
        return(counter)      

obj=Solution()
res=obj.subarraySum([1,1,1],2)
# print(res)