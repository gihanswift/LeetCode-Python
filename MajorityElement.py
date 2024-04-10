class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if count == 0:
                res = i

            count -= -1 if res != i else +1
            print(res)
        return res


obj = Solution()
obj.majorityElement([3, 2, 3])
