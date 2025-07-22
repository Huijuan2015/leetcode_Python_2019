数学解法
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)

        max_freq = max(freq.values())

        max_count = sum(1 for v in freq.values() if v == max_freq) #找出“频率最高”的任务有几个

        part_count = (max_freq-1) * (n + 1) + max_count #?

        return max(len(tasks), part_count)


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_cnt = Counter(tasks)
        #甚至不需要考虑task本人
        heap = [-cnt for cnt in tasks_cnt.values()] #max heap (-cnt, task)
        heapq.heapify(heap)
        res = 0
        while heap:
            tmp = [] # length <= n+1
            for _ in range(n+1):
                if heap:
                    cnt = heapq.heappop(heap)
                    if cnt + 1 < 0:
                        tmp.append(cnt + 1)
                res += 1
                if not heap and not tmp:
                    break
            for item in tmp:
                heapq.heappush(heap, item)
        return res

            
