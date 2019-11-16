class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        numSeen, dotSeen, eSeen, numAfterE = False, False, False, True
        for i, ch in enumerate(s):
            # print ch
            if ch in "0123456789":
                numSeen = True
                numAfterE = True #!!
            elif ch == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif ch =='e':
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numAfterE = False
            elif ch == '+' or ch == '-':
                if i != 0 and s[i-1] != 'e':#+- 不在第一位或者e后面
                    return False
            else:
                return False
        return numSeen and numAfterE








class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
#          Deterministic finite automaton DFA 过滤敏感字
# https://blog.csdn.net/BuptZhengChaoJie/article/details/70332444
#     https://blog.csdn.net/u012601587/article/details/50560838
        state = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True