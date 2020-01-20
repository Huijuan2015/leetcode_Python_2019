class Solution(object):
    def canReach(self, nums, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if not nums:
            return False
        q = collections.deque()
        q.append(start)
        visited = set()
        while q:
            i = q.popleft()
            if nums[i] == 0:
                return True
            visited.add(i)
            if i-nums[i]>=0 and i-nums[i] not in visited:
                q.append(i-nums[i])
            if i+nums[i]<len(nums) and i+nums[i] not in visited:
                q.append(i+nums[i]) 
        return False