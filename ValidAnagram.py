class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        thisset=set()
        thisset1=set()
        for i in s:
            if i not in thisset:
                thisset.add(i)
        for i in t:
            if i not in thisset1:
                thisset1.add(i)
        for i in t:
            s=s.replace(i,"",1)
    
        if thisset==thisset1 and len(s)==0:
            return True
        else:
            return False