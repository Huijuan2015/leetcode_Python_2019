s[i - 1]为0
这种情况下由于0只能与前面的1或2结合才能编码，所以根据情况，若s[i - 2]为1或2则dp[i] = dp[i - 2];
若s[i - 2]为星号则星号表示1和2时满足编码条件则可知dp[i]为dp[i - 2]的两倍
若不是上面两种情况则不可编码返回0

s[i - 1]为星号
对于这种情况星号首先单独表示一个字符则有9种可能，首先我们给dp[i]加上9*dp[i - 1]，
接下来我们分析一下星号与前面的字符结合表示一个字符的编码个数，
若前一个字符即s[i - 2]为1时，星号表示的9个数字均可以与1结合表示一种编码故可为dp[i]加上9 * dp[i - 2]，
若前一个字符即s[i - 2]为2时，星号只有表示1-6这6个数字时才能与2结合表示一种编码故为dp[i]加上6 * dp[i - 2],
若前一个字符即s[i - 2]为号的时候则只有上述两种情况的全部能满足条件故为dp[i]加上15 dp[i - 2],

s[i - 1]为1到9其中一个字符
这种情况下该字符可单独表示一个编码，所以先给dp[i]加上dp[i - 1]，接下来同样地分析与前一个字符的结合情况,
若s[i - 2]为1则任何s[i - 1]均能与其结合表示一种编码故再加上dp[i - 2],
若s[i - 2]为2则只有s[i - 1]为1到6之间能满足编码条件，此时若s[i - 1]为1到6加上dp[i - 2]
若s[i - 2]为星号，若s[i - 1]为1到6则星号表示1和2时能与其结合，此时加上2 * dp[i - 2]，而若s[i - 1]为7到9则只有星号表示1能编码此时加上dp[i - 2]
————————————————
版权声明：本文为CSDN博主「caijhBlog」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/caijhBlog/article/details/78893466

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        dp = [0 for _ in range(n+1)] #dp[i] 第i位有多少种decode ways
        dp[0] = 1
        if s[0] == '0':
            return 0
        if s[0] == '*': ---------------------------------注意初始化
            dp[1] = 9
        else:
            dp[1] = 1
        M = 1000000007
        for i in range(1, n):
            if s[i] == '0': ------------------------------为0的情况要单独考虑
                if s[i-1] == '1' or s[i-1] =='2':
                    dp[i+1] += dp[i-1]
                elif s[i-1] =='*':
                    dp[i+1] = dp[i-1]*2
                else:
                    return 0 -------------------------------一直为0的情况
            elif s[i] == '*':
                
                dp[i+1] += dp[i]*9
                if s[i-1] == '1':
                    dp[i+1] += dp[i-1]*9
                elif s[i-1] == '2':
                    dp[i+1] += dp[i-1]*6
                elif s[i-1] == '*':
                    dp[i+1] += 15*dp[i-1]
            elif s[i] >= '1' and s[i] <= '9':
                dp[i+1] += dp[i]
                if s[i-1] == '1':
                    dp[i+1] += dp[i-1]
                elif s[i-1] == '2' and s[i]<= '6':
                    dp[i+1] += dp[i-1]
                elif s[i-1] == '*' and s[i] >= '1' and s[i]<= '6':
                    dp[i+1] += dp[i-1]*2
                elif s[i-1] == '*' and s[i]> '6':
                    dp[i+1] += dp[i-1]
            dp[i+1] %= M -------------------------------------------------注意取模
        return dp[-1]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        https://blog.csdn.net/caijhBlog/article/details/78893466
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        # i = 0: 
            #i-1 == 1/2 => +=dp[i]
            #i-1= *=> 表示1、2, += 2*dp[i]
        
        # i = *:
            # += 9*dp[i-1]
            # i-1 = 1/2 => 1: += dp[i-1]*9; 2: dp[i-1]*6
            # i-1 =*: + dp[i-1]*15 (1/2)
        #i == 1~9:
            # += dp[i-1](单独)
            # i-1 = 1 => +=dp[i-1]
            # i-1 = 2 => i<=6 => +=dp[i-1]
            # i-1 = * => 
                # i<=6 => 只有当 i-1=1/2 => +=2* dp[i-1]
                # i>6 => 只有当i-1=1 => +=dp[i-1] 
        
        for i in range(len(s)):
            if s[i] == '0':
                if i-1>=0 and (s[i-1] == '1' or s[i-1] == '2'):
                    dp[i+1] += dp[i-1] 
                if i-1>=0 and s[i-1] == '*':
                    dp[i+1] += 2*dp[i-1]
            elif s[i] == '*':
                dp[i+1] += 9*dp[i]
                if i-1>=0 and s[i-1] == '1':
                    dp[i+1] += 9*dp[i-1]
                elif i-1>=0 and s[i-1] =='2':
                    dp[i+1] += 6*dp[i-1]
            else:
                dp[i+1] += dp[i]
                if i-1>=0 and s[i-1] == '1':
                    dp[i+1] += dp[i-1]
                elif i-1>=0 and s[i-1] =='2' and int(s[i]) <= 6:
                    dp[i+1] += dp[i-1]
                elif i-1>=0 and s[i-1] == '*':
                    if int(s[i]) <= 6:
                        dp[i+1] += 2*dp[i-1]
                    else:
                        dp[i+1] += dp[i-1]
        return dp[len(s)]

            