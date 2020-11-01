class Solution:
    def findMax(self,s,low,high,start,maxlen) -> (int,int):
        length = len(s)
        while low>=0 and high<length and s[low]==s[high]:
            if high-low+1 > maxlen:
                start, maxlen = low, high-low+1
            low-=1
            high+=1
        return start,maxlen
    
    def longestPalindrome(self, s: str) -> str:
        start, maxlen = 0, 1
        low, high = 0, 0
        length = len(s)
        for i in range(1,length):
            lowX=[i-1,i-1]
            highX=[i,i+1]
            for index in range(0,len(lowX)):
                start, maxlen = self.findMax(s, lowX[index], highX[index], start, maxlen)
        return s[start:start+maxlen]        
            
    
#print(Solution().longestPalindrome("aqaqa"))
print(Solution().longestPalindrome("aqaatqa"))