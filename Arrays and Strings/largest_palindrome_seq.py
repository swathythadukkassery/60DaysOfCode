class Solution:
    def fun(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        
        return r-l-1
    def longestPalindrome(self, s: str) -> str:
        start,end=0,0
        for i in range(len(s)):
            len1=self.fun(s,i,i)
            len2=self.fun(s,i,i+1)
            lenFinal=max(len1,len2)
            if lenFinal>end-start:
                start=i-int((lenFinal-1)/2)
                end=i+int(lenFinal/2)
       
        return s[start:end+1]

#         m = ''  
#         for i in range(len(s)):  
#             for j in range(len(s), i, -1): 
                
#                 if len(m) >= j-i :  
#                     break
                    
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m
        
        