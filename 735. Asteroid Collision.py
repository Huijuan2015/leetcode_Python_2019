class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk = []
        for asteroid in asteroids:
            while stk and asteroid < 0 and stk[-1] > 0:
                # top 小
                if stk[-1] < -asteroid:
                    stk.pop()
                    # continue
                # top 等
                elif stk[-1] == -asteroid:
                    stk.pop()
                    break
                # top 大
                else:
                    break
            else:
                stk.append(asteroid)
        return stk
                    