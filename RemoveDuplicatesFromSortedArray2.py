class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            print("hey")
            r += 1
        return l

        # l = 1
        # for r in range(1, len(nums)):
        #     print(r)
        #     if nums[r] != nums[r-1]:
        #         nums[l] = nums[r]
        #         l += 1
        #
        #
        # return l



sol = Solution()
sol.removeDuplicates([1,1,1,2,2,3])

for i in range(min(3, 4)):
    print(i)