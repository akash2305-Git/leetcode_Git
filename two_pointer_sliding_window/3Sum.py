

class threeSum:

    def add_three(self,nums):

        result = []
        nums.sort()

        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return result




if __name__ == "__main__":

    ts = threeSum()
    nums = [-1,0,1,2,-1,-4]
    ans = ts.add_three(nums)
    nums1= [0,1,1]
    ans1 = ts.add_three(nums1)
    print(ans)
    print(ans1)



