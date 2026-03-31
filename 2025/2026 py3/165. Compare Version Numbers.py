class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1, n2 = len(v1), len(v2)
        l =  max(n1, n2)
        for i in range(l):
            # 拿到原始字符串（处理越界）
            num1 = int(v1[i]) if i < n1 else 0
            num2 = int(v2[i]) if i < n2 else 0

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        return 0

1.01和1.001是相同的版本

如果规定是不同的版本
那在最后

if num1 < num2:
    return -1
elif num1 > num2:
    return 1

比较长度
# 3. 如果数值相等，则比较原始字符串的长度
            # 假设规则是：001 > 01 (长度长的更大)
            if len(v1[i]) > len(v2[i]):
                return 1
            elif len(v1[i]) < len(v2[i]):
                return -1