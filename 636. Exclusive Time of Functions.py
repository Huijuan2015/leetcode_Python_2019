class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # stack
        ans = [0] *n
        stk = []
#similar to the closing openning backet problems, where there's nesting, stack is required
# nested function time need to be deducted from the parent time, therefore update the parent function with negative children's time
# Each time a function finishes, the time span needs to be added to the function slot in the outputs array
        for s in logs:
            tokens = s.split(":")
            id, state, time = int(tokens[0]), tokens[1], int(tokens[2])
            if state == "start":
                stk.append((id, time))
            else:
                id_end, time_start = stk.pop()
                diff = time - time_start + 1
                ans[id_end] += diff
                if len(stk) > 0:
                    ans[stk[-1][0]] -= diff
        return ans
        
https://blog.csdn.net/qq_26410101/article/details/81838342

既然要分解计算出函数的独立运行时间，那么我们就必须在函数之间插入阻断标志，比如题目给的示例：

["0:start:0",

"1:start:2",

"1:end:5",

"0:end:6"]

我们应该更新为如下形式：

["0:start:0",

"0:end:0",

"1:start:2",

"1:end:5",

"0:start:6",

"0:end:6"]
