class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        res, i, sign = 0, 0, 1

        INT_MAX = 2**31-1
        INT_MIN= -2**31

        #space
        while i < len(s)  and s[i] == " ":
            i += 1

        #sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if res > (INT_MAX-digit)//10:  #这里要注意
                return INT_MAX if sign == 1 else INT_MIN

            res = res*10+digit
            i +=1

        return min(res*sign, INT_MAX) if sign == 1 else max(INT_MIN, res*sign)
        

            
