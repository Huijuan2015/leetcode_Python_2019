class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(v) for v in version1.split('.')]
        version2 = [int(v) for v in version2.split('.')]
        i = 0
        for i in range(max(len(version1), len(version1))):
            v1 = version1[i] if i < len(version1) else 0
            v2 = version2[i] if i < len(version2) else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def removeZero(s):
            while len(s) > 1 and s[0] == '0':
                s = s[1:]
            return int(s)
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0
        while i < len(v1) and i < len(v2):
            if removeZero(v1[i]) > removeZero(v2[i]):
                return 1
            elif removeZero(v1[i]) < removeZero(v2[i]):
                return -1     
            i += 1
        while i < len(v1) and removeZero(v1[i]) == 0:
            i += 1
        if i < len(v1):
            return 1
        while i < len(v2) and removeZero(v2[i]) == 0:
            i += 1
        if i < len(v2):
            return -1
        return 0