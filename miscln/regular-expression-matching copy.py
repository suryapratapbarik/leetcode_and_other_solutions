class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si, pi = 0,0
        while pi<len(p):
            if pi+1<len(p) and p[pi+1]=='*':
                while si<len(s):
                    if s[si]==p[pi] or p[pi]=='.':
                        if self.isMatch(s[si:],p[pi+2:]):
                            return True
                        si+=1
                    else:
                        break
                pi+=2
            elif pi<len(p) and si<len(s) and (p[pi]=='.' or p[pi]==s[si]):
                pi+=1
                si+=1
            else:
                return False
        return si==len(s)
    
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