Union find
class Solution(object):
    def removeStones(self, points):
        UF = {}
        def find(x):
            if x != UF[x]:
                print x, UF[x]
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x) # UF[x] = x if key x not exists
            UF.setdefault(y, y)
            print x, y, UF, find(x), find(y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j) # ~ 用来区分 x y
            # print UF
        
        return len(points) - len({find(x) for x in UF})


DFS, 找联通，

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        mpx = collections.defaultdict(set)
        mpy = collections.defaultdict(set)
        for stone in stones:
            x, y = stone
            mpx[x].add(y)
            mpy[y].add(x)
        def dfsx(x):
            seenX.add(x)
            for y in mpx[x]:
                if y not in seenY:
                    dfsy(y)
                
        def dfsy(y):
            seenY.add(y)
            for x in mpy[y]:
                if x not in seenX:
                    dfsx(x)
                
        seenX, seenY = set(), set() 
        island = 0
        #find islands
        for x, y in stones:
            if x not in seenX:
                island += 1
                dfsx(x)
                dfsy(y)
        return len(stones)-island