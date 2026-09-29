class Solution:
    def isPalindrome(self, s: str) -> bool:
        os=""
        for ch in s:
            if ch.isalnum():
                os += ch.lower()
        
        p=0
        q=len(os)-1
        while(p<q):
            if(os[p]!=os[q]):
                return False
            p+=1;
            q-=1;
        return True