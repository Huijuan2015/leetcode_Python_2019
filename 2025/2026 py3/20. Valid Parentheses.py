class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch in "([{":
                stk.append(ch)
            elif ch in ")]}":
                if stk:
                    top = stk.pop()
                    #可以做个map {):(,...}
                    if (top == '(' and ch !=')') or (top == '{' and ch !='}') or (top == '[' and ch !=']'):
                        return False
                else:
                    return False
            else:
                return False
        # return True if not stk else False
        return not stk