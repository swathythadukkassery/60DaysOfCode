from collections import defaultdict
class Solution:   
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dicti=defaultdict()
        nums.sort()
        n=len(nums)
        count=0
        for i in range(n-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while(j<k):
                threesum=nums[i]+nums[j]+nums[k]
                if threesum>0:
                    k-=1
                elif threesum<0:
                    j+=1
                else:
                    if  nums[j]==nums[j-1] and j-1!=i :
                        j+=1
                        k-=1
                    else:
                        dicti[count]=[nums[i],nums[j],nums[k]]
                        j+=1
                        k-=1
                        count+=1
                    
                    
        return dicti.values()