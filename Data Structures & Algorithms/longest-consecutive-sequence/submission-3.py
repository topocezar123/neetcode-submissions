class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        aparitii = set(nums) 
        maxim_global = 0 
      
        for num in aparitii:
            
           
            if (num - 1) not in aparitii:
                
                lungime_curenta = 1
                urmatorul = num + 1
                
              
                while urmatorul in aparitii:
                    lungime_curenta = lungime_curenta + 1
                    urmatorul = urmatorul + 1
                
                
                if lungime_curenta > maxim_global:
                    maxim_global = lungime_curenta
                    
        return maxim_global