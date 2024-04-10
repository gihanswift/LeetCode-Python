class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            # 3 > 6
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
        print(nums1)




obj = Solution()
obj.merge([1,2,3,0,0,0], 3, [3,2,3,0,0,0], 3)