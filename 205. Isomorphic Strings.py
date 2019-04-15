class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # hashmap = {}
        # for i in xrange(len(s)):
        #     if s[i] not in hashmap:
        #         hashmap[s[i]] = t[i]
        #     elif hashmap[s[i]] != t[i]:
        #         return False
        # mapval = [hashmap[k] for k in hashmap]
        # return len(mapval) == len(set(mapval))
 
        #return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        #"foo""bar" -> set(zip(s, t) -> [(u'f', u'b'), (u'o', u'a'), (u'o', u'r')]
        # return map(s.find, s) == map(t.find, t)