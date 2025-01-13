



'''

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


'''
from typing import List


class jump_Game:


    def min_jump(self,nums: List[int]) -> int :

        jump , count , last = 0,0,0

        for i in range(0,len(nums)-1):
            jump = max(jump,i+nums[i])
            if i == last:

                last = jump

                count += 1

        return count



if __name__ == "__main__":


    nums = [2,3,1,1,4]

    jg = jump_Game()

    ans = jg.min_jump(nums)

    print("The number of jumps required is",ans)
