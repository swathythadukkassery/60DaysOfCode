import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f,s=math.inf,math.inf
        for i in range(len(nums)):
            if f>nums[i]:
                f=nums[i]
            elif s>nums[i] and f<nums[i] :
                s=nums[i]
            elif nums[i]>s:
                return True
        return False