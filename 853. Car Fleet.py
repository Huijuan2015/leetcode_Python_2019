class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        res, curr = 0, 0.0
        posToTime = {}
        for pos, spd in sorted(zip(position, speed)): #buyong
            posToTime[-pos] = float(target-pos)/spd
        print posToTime
        for k in  sorted(posToTime.keys()):   从位置最靠近target的position开始，不会超车，如果用时小于curr，说明降过速，与前一个算一个车队
            print k, posToTime[k], curr
            if  posToTime[k] <= curr:
                continue
            curr = posToTime[k]
            res += 1
        return res