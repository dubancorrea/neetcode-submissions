class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## It contains the same amount of letters and same letters no matter the order
        ## We can check first if both have the same lenght
     

        if len(t) != len(s):
            return False
        
        return sorted(s) == sorted(t)