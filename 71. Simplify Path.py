class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
#         中间是"."的情况直接去掉，
#         是".."时删掉它上面挨着的一个路径，
#         如果是空的话返回"/"，
#         如果有多个"/"只保留一个。
#         那么我们可以把路径看做是由一个或多个"/"分割开的众多子字符串，把它们分别提取出来一一处理即可
        
#         .:不操作
#         ..: 弹栈
        stk = []
        i = 0
        while i < len(path):
            end = i+1
            while end < len(path) and path[end] != '/':
                end += 1
            sub = path[i+1: end]
            if len(sub) > 0:
                if sub =="..":
                    if stk:
                        stk.pop()
                elif sub != ".":
                    stk.append(sub)
            i = end
        if not stk:
            return '/'
        return  '/' + '/'.join(stk)