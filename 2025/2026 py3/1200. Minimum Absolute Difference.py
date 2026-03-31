class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        #sort完了，一组一组编里，keep min absolute diff 值
        diff = float('inf')
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == diff:
                res.append([arr[i-1], arr[i]])
            elif arr[i] - arr[i-1] < diff:
                res = [[arr[i-1], arr[i]]]
                diff = arr[i] - arr[i-1]
        return res
