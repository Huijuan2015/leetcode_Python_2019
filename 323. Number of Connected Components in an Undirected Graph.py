class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 0:1---1
        # 1:2,0---2
        # 2:1---1
        # 3:4---1
        # 4:3---1
        graph = collections.defaultdict(set)
        
        for edge in edges:
            p1, p2 = edge
            graph[p1].add(p2)
            graph[p2].add(p1)
        cnt  = 0 
        seen = set()
        
        for i in range(n):
            if i not in seen:
                q = [i]
                for node in q:
                    for nbr in graph[node]:
                        if nbr not in seen:
                            seen.add(nbr)
                            q.append(nbr)
                cnt += 1
   
        return cnt