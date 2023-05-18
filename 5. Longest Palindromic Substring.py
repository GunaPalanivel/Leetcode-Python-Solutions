class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            # Check for odd-length palindromes centered at i
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > end - start + 1:
                    start, end = l, r
                l -= 1
                r += 1
            # Check for even-length palindromes centered at i and i+1
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > end - start + 1:
                    start, end = l, r
                l -= 1
                r += 1
        return s[start:end+1]
