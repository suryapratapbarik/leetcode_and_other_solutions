class Solution:
    def isMatch(self, s: str, p: str, cond=True) -> bool:
        if cond==True:
            s, p = s[::-1], p[::-1]
        si, pi = 0,0
        while pi<len(p):
            if int(pi+1)<int(len(p)) and p[pi]=='*':
                while si<len(s):
                    if s[si]==p[pi+1] or p[pi+1]=='.':
                        if self.isMatch(s[si:],p[pi+2:], False):
                            return True
                        si+=1
                    else:
                        break
                pi+=2
            elif pi<len(p) and si<len(s) and p[pi]=='.':
                pi+=1
                si+=1
            elif pi<len(p) and si<len(s) and p[pi]==s[si]:
                pi+=1
                si+=1
            else:
                return False
        if si==len(s):
            return True
        return False
    
print (Solution().isMatch("aa","a*"))
print (Solution().isMatch("aaa","a*a"))
print (Solution().isMatch("ab",".*c"))
print (Solution().isMatch("aaa","aaaa"))
print (Solution().isMatch("aab","c*a*b")) 
print (Solution().isMatch("aaa","ab*a*c*a"))
print (Solution().isMatch("aa","ac*a*"))
print (Solution().isMatch("a","c*a*"))
print (Solution().isMatch("aasdfasdfasdfasdfas","aasdf.*asdf.*asdf.*asdf.*s"))

"aasdfasdfasdfasdfas"
"aasdf.*asdf.*asdf.*asdf.*s"

#b*a*c, baa
#c*., ba
#*aba, aaaba