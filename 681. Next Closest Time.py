class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def isValid(time):
            return int(time[:2]) < 24 and int(time[2:]) < 60
        time = time[:2] + time[3:]
        stime = sorted(time)
        
        for i in (3,2,1,0):
            for t in sorted(stime):
                if t > time[i]: #当当前位数字小于 stime的数字时
                    # 改变当前位，并且后面都置为最小
                    newTime = time[:i]+ t + stime[0] * (3 - i)
                    if isValid(newTime):
                        return newTime[:2]+':'+newTime[2:]
        #都不满足条件
        return stime[0]*2+':'+stime[0]*2

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        time = time[:2] + time[3:]
        isValid = lambda t: int(t[:2]) < 24 and int(t[2:]) < 60
        stime = sorted(time)
        for x in (3, 2, 1, 0):
            for y in stime:
                if y <= time[x]: continue
                ntime = time[:x] + y + (stime[0] * (3 - x))
                # print (x, y, (stime[0] * (3 - x)), ntime)
                if isValid(ntime):return ntime[:2] + ':' + ntime[2:]
        return stime[0]*2 + ':' + stime[0]*2
        