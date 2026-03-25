
# leetcode - 350

class Solution:
    def intersection(self, num1, num2):
        num1.sort()
        num2.sort()

        res = []
        i=0
        j=0

        while i < len(num1) and j < len(num2):
            if num1[i] < num1[j]:
                i+=1
            elif num1[i] > num2[j]:
                j+=1
            else:
                res.append(num1[i]))
                i+=1
                j+=1
        return res

