class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map =  {}
        res = len(list1) + len(list2)#1e9
        ret = []
        for i in xrange(len(list1)):
            index_map[list1[i]] = i
        #index_map = {u: i for i, u in enumerate(A)}
        for i in xrange(len(list2)): #for j, v in enumerate(B): (index use enumerate)
            tmp = -1
            if not index_map.has_key(list2[i]):
                continue
            else:
                tmp = i + index_map[list2[i]]
                if res > tmp:
                    res = tmp
                    ret = [list2[i]]
                elif res == tmp:
                    ret.append(list2[i])       
        return ret


def findRestaurant(self, A, B):
    Aindex = {u: i for i, u in enumerate(A)}
    best, ans = 1e9, []

    for j, v in enumerate(B):
        i = Aindex.get(v, 1e9)#default 1e9
        if i + j < best:
            best = i + j
            ans = [v]
        elif i + j == best:
            ans.append(v)
    return ans