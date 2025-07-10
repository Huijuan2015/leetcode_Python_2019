class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
    #     简化规则如下：
	# •	. 表示当前目录 → 可以忽略
	# •	.. 表示返回上一级目录 → 栈中弹出一个目录（如果有）
	# •	多个 / 合并成一个 /
	# •	最终路径必须以 / 开头，不包含多余的 /
	# •	不能越出根目录（/.. 等价于 /）
        parts = path.split('/')
        stk = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(part)
        return '/'+'/'.join(stk)