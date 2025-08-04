class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += 'I'
        letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        i = 0
        while i < len(s) - 1:
            if letters[s[i]] >= letters[s[i + 1]]:
                count += letters[s[i]]
                i += 1
            else:
                count += letters[s[i + 1]] - letters[s[i]]
                i = i + 2

        return count

print(Solution().romanToInt("MCMXCIV"))