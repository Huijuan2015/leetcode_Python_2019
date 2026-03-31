class Solution:
    def simplifyPath(self, path: str) -> str:
        # . 忽略
        # ..上一级， 弹出
        # // 合并/
        # ...
        parts = path.split('/')
        stk = []

        for part in parts:
            if part == '.' or part == '':
                # 不压入，忽略, 比如 / / 分成‘’
                continue
            elif part =='..':
                if stk:
                    stk.pop()
            else:
                stk.append(part)
        return '/' +'/'.join(stk)