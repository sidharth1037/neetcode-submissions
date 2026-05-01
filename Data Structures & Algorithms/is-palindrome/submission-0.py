class Solution:
    def isPalindrome(self, s: str) -> bool:

        alnums = "".join(filter(str.isalnum, s)).lower()
        length = len(alnums)

        for i in range(length//2):
            if alnums[i] != alnums[length-i-1]:
                return False

        return True