class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        #build graph mp,  parent mp
        from collections import defaultdict
        from collections import deque
        succ_mp = defaultdict(list)
        parents_mp = {}
        # update parent mp in one pass - necessary for avoiding a lot edge case of parent char missing
        for word in words:
            for ch in word:
                parents_mp[ch] = 0
            
        for i in range(1, len(words)):
            w1, w2 = words[i-1],words[i]
            j = 0
            while j < len(w1) and j < len(w2) and w1[j] == w2[j]:
                j += 1
            if j < len(w1) and j < len(w2) and w1[j] != w2[j]:
                succ_mp[w1[j]].append(w2[j]) # update succ children   
                parents_mp[w2[j]] += 1 #update parents count
                
        res =  ""
        q = deque()
        for k, v in parents_mp.items():
            if v == 0:
                q.append(k)  
        
        while q:
            curr = q.popleft() 
            res += curr
            if curr not in succ_mp:
                continue
            succs = succ_mp[curr]
            for succ in succs:
                if parents_mp[succ] == 1:
                    parents_mp[succ] == 0
                    q.append(succ)
                parents_mp[succ] -= 1
            
        return res if len(res) == len(parents_mp) else ""
        
    
                
            
                
                