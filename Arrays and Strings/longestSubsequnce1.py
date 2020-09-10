class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hashs=[]
        p=0
        curmax,i,j=0,0,0
        while i<n and j<n:
            # print("ij",i,j,curmax)
            if s[j] not in hashs:
                hashs.append(s[j])
                j+=1
                curmax=max(curmax,j-i)
            else:
                p=hashs.index(s[j])+1
                hashs=hashs[p:]
                hashs.append(s[j])
                j+=1
                i+=p
        return curmax