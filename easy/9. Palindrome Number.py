class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        for i in range(0, len(x_str) // 2 + len(x_str) % 2):
            if x_str[i] != x_str[len(x_str) - i - 1]:
                return False
        return True