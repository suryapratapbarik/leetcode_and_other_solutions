class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        period = 2*(numRows-1)
        lines={}
        for line_no in range(1,numRows+1):
            loop_no=0
            maxIndex=0
            while maxIndex<len(s):
                if not (line_no in lines and isinstance(lines[line_no], list)):
                    lines[line_no]=[]
                if line_no==1 or line_no==numRows:
                    nextNum = line_no + period*loop_no
                    lines[line_no].append(nextNum)
                    maxIndex = max([maxIndex, nextNum])
                else:
                    nextNum = line_no + period*loop_no
                    nextOfNextNum = line_no + period*(loop_no+1) - 2*(line_no-1)
                    lines[line_no].append(nextNum)
                    lines[line_no].append(nextOfNextNum)
                    maxIndex = max([maxIndex, nextOfNextNum])
                loop_no+=1
        result=""
        for n in range(1,numRows+1):
            #print(n,"->",lines[n])
            for charIndex in range(0,len(lines[n])):
                if lines[n][charIndex] <= len(s):
                    #print(lines[n][charIndex], s[lines[n][charIndex]-1])
                    result+=s[lines[n][charIndex]-1]
        return result
                    

print(Solution().convert("ABcdefgh",1))
print(Solution().convert("ABcdefgh",2))                    
print(Solution().convert("123456789abcdefghijk",4))
print(Solution().convert("123456789abcdefghijk",5))
print(Solution().convert("123456789abcdefghijk",6))
print(Solution().convert("",1))
print(Solution().convert("A",1))