class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecventa={}
        for num in nums:
            if num in frecventa:
             frecventa[num]=frecventa[num]+1
            else:
             frecventa[num]=1
        numere_sortate=sorted(frecventa,key=lambda x:frecventa[x],reverse=True)    
        return numere_sortate[:k]
     

