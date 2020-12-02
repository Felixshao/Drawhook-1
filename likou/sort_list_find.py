# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        try:
            start_position = nums.index(target)
            print(start_position)
        except ValueError:
            return [-1, -1]
        right_nums: list = nums[start_position+1:]
        end = 0
        for i in range(len(right_nums)):
            if right_nums[len(right_nums) - i - 1] == target:
                end = len(right_nums) - i
                break

        end_position = end + start_position
        return [start_position, end_position]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:

        try:
            start_position = nums.index(target)
            end_position = self.get_end_position(nums, target, start_position)
            return [start_position, end_position]
        except ValueError:
            return [-1, -1]

    def get_end_position(self, nums, target, end_position):
        # [1,2,2,2,3,4] 2, 1
        # [1,2] [2,2,3,4] 2, 0
        # [2] [2,3,4] 2, 0

        if nums.count(target) > 1:
            right_nums: list = nums[end_position + 1:]
            end = nums.index(target)
            end_position += end
            self.get_end_position(right_nums, target, end)
        else:
            return end_position


if __name__ == '__main__':

    lis = [5,7,7,8,8,10]
    a = Solution().searchRange2(lis, 8)
    print(a)