class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Trebuie să inițializăm variabila ca un string gol
        text = "" 
        
        for char in s:
            
            if char.isalnum():
                text = text + char.lower()

       
        text_inversat = "".join(reversed(text))

       
        if text == text_inversat:
            return True
            
        return False