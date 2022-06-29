class Solution(object):
    def romanToInt(self, s):
        num = 0
        flagDic = {
            'I': 0,
            'X': 0,
            'C': 0
        }
        romanDic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        falgLett = ['I', 'X', 'C']
        for i in range(len(s)):
            symbol = s[len(s)]
            if symbol in falgLett & flagDic[symbol] != 0:
                num -= romanDic[symbol]
            else:
                num += romanDic[symbol]
                flagDic[symbol] = 1
            s = s[0:len(s)]
        return num
        """
        :type s: str
        :rtype: int
        """
