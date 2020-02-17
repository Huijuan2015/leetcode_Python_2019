Without reversing the string, print it in reverse order.

for example:
s : "321"
Output: "One Hundred Twenty Three"


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        n2w = {1e9:"Billion", 1e6:"Million", 1e3:"Thousand", 1e2:"Hundred",
               90:  "Ninety", 80:  "Eighty", 70:  "Seventy", 60:  "Sixty",
               50:  "Fifty", 40:  "Forty", 30:  "Thirty", 20:  "Twenty",
               19: "Nineteen", 18:  "Eighteen", 17: "Seventeen", 16: "Sixteen",
               15:  "Fifteen", 14: "Fourteen", 13: "Thirteen", 12:  "Twelve",
               11:  "Eleven", 10:  "Ten", 9:   "Nine", 8:"Eight", 7:   "Seven",
               6:   "Six", 5:   "Five", 4: "Four", 3: "Three",
               2: "Two", 1: "One", 0: "Zero" }
        keys = [1000000000, 1000000, 1000, 100, 90, 80, 70,
               60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12,
               11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        def helper(n):
            if n <= 20:
                return n2w[n]
            for div in keys:
                divisor, remain = n//div, n%div # divmod(n, div)
                if not divisor: continue
                s1 = helper(divisor) + " " if div >= 100 else "" #100以上要重新dfs看具体是什么
                s2 = " " + helper(remain) if remain else ""
                return s1 + n2w[div] + s2 #组成
        return helper(num)
                
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def words(n):
            if n < 20:
                return to19[n-1:n] # case 0
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'