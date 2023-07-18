class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower();
        lst=[]
        for i in s:
            if i.isalnum():
                lst.append(i)
        final_str="".join(lst)
        reverse=""
        for i in range(len(final_str)):
            reverse+=(final_str[-1-i])
        return reverse==final_str

        