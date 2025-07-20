while else

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk = []
        for asteroid in asteroids:
            while stk and asteroid < 0 < stk[-1]:
                if asteroid + stk[-1] < 0:
                    stk.pop()
                    continue
                elif asteroid + stk[-1] == 0:
                    stk.pop()
                    break
                else:
                    break
                
            else:
                stk.append(asteroid)
        return stk


如果不用while else

for a in asteroids:
    collided = False
    while stack and a < 0 < stack[-1]:
        if stack[-1] < -a:
            stack.pop()
        elif stack[-1] == -a:
            stack.pop()
            collided = True
            break
        else:
            collided = True
            break
    if not collided:
        stack.append(a)