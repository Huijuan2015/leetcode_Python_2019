class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        i, j, k = 0, 0, 0
        res = []
        if not arr1 or not arr2 or not arr3:
            return res
        while i<len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif min(arr1[i], arr2[j], arr3[k]) == arr1[i]:
                i += 1
            elif min(arr1[i], arr2[j], arr3[k]) == arr2[j]:
                j += 1
            elif min(arr1[i], arr2[j], arr3[k]) == arr3[k]:
                k += 1
                
                
        return res




            if (arr1[i] == arr2[j] && arr2[j] == arr3[k]) {
                result.add(arr1[i]);
                i++;
                j++;
                k++;
            } else if (arr1[i] < arr2[j]) {
                i++;
            } else if (arr2[j] < arr3[k]) {
                j++;
            } else k++;