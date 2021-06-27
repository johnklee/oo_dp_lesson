class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i, pl = s.find(part), len(part)
        while i >= 0:
            s = s[0:i] + s[i+pl:]
            i = s.find(part)
            
        return s
