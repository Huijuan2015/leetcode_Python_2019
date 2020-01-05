class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.helper(num, 0, 0, 0, 0, target, "")
        return self.res
    # curr: curr holding number, only used for when extend number
    # prev: last digit
    # value: prev add up result
    def helper(self, num, idx, prev, curr, value, target, path):
        
        if idx == len(num) and value == target and curr == 0:
            print idx, curr, value, path
            self.res.append(path[1:])
            return
        if idx == len(num):
            return
        curr = curr*10+int(num[idx])
        # extend
        if curr > 0:
            self.helper(num, idx+1, prev, curr, value, target, path)
        # +
        self.helper(num, idx+1, curr, 0, value+curr, target, path+"+"+ str(curr))

        if len(path) > 0: # 不用idx>0，*10+5，
            # -
            self.helper(num, idx+1, -curr, 0, value-curr, target, path+"-"+ str(curr))
            # *
            self.helper(num, idx+1, curr*prev, 0, (value-prev)+prev*curr, target, path+"*"+ str(curr))
            
            
            
            