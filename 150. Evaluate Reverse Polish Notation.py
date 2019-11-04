class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 遇到数字-入栈，遇到运算：出栈，运算，结果入栈
        stk = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stk.append(int(token))
            else:
                # print 5/2, 5//2, 5/-2, 5//-2, 1/-22, 1//-22
                num2 = stk.pop()
                num1 = stk.pop()
                # print num1, num2, token, stk
                if token == "+":
                    stk.append(num1+num2)
                elif token == "-":
                    stk.append(num1-num2)
                elif token == "*":
                    stk.append(num1 * num2)
                elif token == "/":
                    # num = num1//num2 if num1//num2 >=0 else (num1//num2+1)
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    if num1*num2 < 0 and num1 % num2 != 0:
                        stk.append(num1/num2+1)
                    else:
                        stk.append(num1/num2)
                    # print num
                    # stk.append(num)
            
        return stk.pop()


for i in tokens:
        try:
            temp = int(i)
            stack.append(temp)
        except Exception, e:         
            b,a=stack[-1],stack[-2]
            stack.pop()
            stack.pop()
            if i == '+':    a = a+b
            elif i=='-':    a = a-b
            elif i=='*':    a = a*b
            elif i=='/':    a = int(a*1.0/b)
            stack.append(a)