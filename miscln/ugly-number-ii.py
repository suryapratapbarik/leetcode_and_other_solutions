class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        i2 = i3= i5 = 0;
        while n > 1:
            u2, u3, u5 = 2*uglyNums[i2], 3*uglyNums[i3], 5*uglyNums[i5]
            uMin = min(u2,u3,u5)
            if uMin == u2: i2+=1
            if uMin == u3: i3+=1
            if uMin == u5: i5+=1
            uglyNums.append(uMin)
            n -=1
        return uglyNums[-1]
            
print (Solution().nthUglyNumber(54))