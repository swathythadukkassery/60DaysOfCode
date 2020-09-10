class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res, dic = 0, defaultdict(lambda:0)
        for a in A:
            for b in B:
                dic[a+b] += 1
        for c in C:
            for d in D:
                res += dic[0 - (c + d)]
        return res   