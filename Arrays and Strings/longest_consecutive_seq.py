class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curmax=0
        orgmax=0
        numss=set(nums)
        for num in nums:
            if num-1 not in numss:
                curnum=num
                curmax=1
                while curnum + 1 in numss:
                    curmax+=1
                    curnum+=1
                orgmax=max(curmax,orgmax)
        return orgmax