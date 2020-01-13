class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # a:3 b:1
        import heapq
        import collections
        pq = [(-cnt, ch) for ch, cnt in collections.Counter(S).items()]
        for cnt, ch in pq:
            # print cnt
            if -cnt > (len(S)+1)/2:
                return ""
            
        # print pq
        ans = ""
        heapq.heapify(pq)
        while len(pq)>=2:
            cnt1, ch1 = heapq.heappop(pq)
            cnt2, ch2 = heapq.heappop(pq)
            ans += ch1+ch2
            if cnt1+1:
                heapq.heappush(pq, (cnt1+1, ch1))
            if cnt2+1:
                heapq.heappush(pq, (cnt2+1, ch2))
        if pq:
            ans += heapq.heappop(pq)[1]
        return ans
            


        解法2， 不用heapq， 用数组记住count和字母
        由于字母需要排序，所有长度26的数组排序后无法记住是哪个字母
        count*100 + 字母
        ex. 
        3 个 a:记成 300 
        2 个 b::201