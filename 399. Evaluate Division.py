class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # build graph and bfs
        graph = collections.defaultdict(lambda: collections.defaultdict())
        for equation, value in zip(equations, values):
            ch1, ch2 = equation
            graph[ch1][ch2] = value
            graph[ch2][ch1] = 1.0/value
            graph[ch1][ch1] = 1.0
            graph[ch2][ch2] = 1.0
        res = []
        for querie in queries:
            ch1, ch2 = querie
            curr = -1.0
            q = collections.deque()
            visited = set()
            q.append((ch1, 1.0))
            
            while q:
                ch, v = q.popleft()
                if ch not in graph:
                    break
                if ch == ch2:
                    curr = v
                    break
                visited.add(ch)
                for nbrc, nbrv in graph[ch].items():
                    if nbrc not in visited:
                        q.append((nbrc, v*nbrv))
            res.append(curr)
        return res
                
        
            
            