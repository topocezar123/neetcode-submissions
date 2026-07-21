class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     n = len(nums)
     rezultat=[1]*n

     stanga=1
     for i in range(n):
        rezultat[i]=stanga
        stanga=stanga* nums[i]

     dreapta=1
     for i in reversed(range(n)):
        rezultat[i]=rezultat[i]*dreapta
        dreapta=dreapta*nums[i]
     return rezultat

        
