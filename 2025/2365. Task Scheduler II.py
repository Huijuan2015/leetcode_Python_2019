class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        last_exec = {}
        time = 0

        for task in tasks:
            if task in last_exec and time < last_exec[task] + space + 1:
                # 把当前时间 time “更新为合法的最早可执行时间”
                time = last_exec[task] + space + 1
            last_exec[task] = time
            time += 1
        return time