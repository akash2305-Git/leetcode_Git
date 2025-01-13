

'''
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.

'''





class Jump_Game:

    '''
    def jump(self,nums):

        ans = 0

        for i in nums:
            if ans < 0:
                return False
            elif i>ans:
                ans = i
            ans -= 1

        return True

    '''

    def jump(self,nums):

        curr = nums[0]

        for i in range(1,len(nums)):

            if curr == 0:
                return False

            curr -= 1
            curr = max(curr,nums[i])
        return True




if __name__ == "__main__":
    nums = [2,3,1,1,4]
    #nums = [3,2,1,0,4]
    jg = Jump_Game()

    ans = jg.jump(nums)

    if ans:
        print("It can reach to max index")
    else:
        print("It can't reach to max index")
