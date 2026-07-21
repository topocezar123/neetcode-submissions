class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictionar = {} 
        
        for cuvant in strs:
            
            semnatura = "".join(sorted(cuvant))
            
           
            if semnatura not in dictionar:
                dictionar[semnatura] = [] 
                
           
            dictionar[semnatura].append(cuvant)
            
       
        return list(dictionar.values())