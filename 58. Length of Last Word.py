class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lists=s.split()
        lastword=lists[-1]
        index=len(lastword)
        return index
        