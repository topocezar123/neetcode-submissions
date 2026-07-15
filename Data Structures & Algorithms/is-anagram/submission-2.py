class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sortat=sorted(s)
        t_sortat=sorted(t)
        if s_sortat!=t_sortat:
            return False
        return True

        
         
        

       