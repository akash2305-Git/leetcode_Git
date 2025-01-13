
'''

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''


class intersection_of_Two_Array:

    '''
    Hash Map Solution using python Dict


    def intersection(self,nums1,nums2):

        freq = {}
        for i in nums1:

            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        ans = []

        for i in nums2:
            if i in freq and freq[i]>0:
                ans.append(i)
                freq[i] -= 1

        return ans

    '''


    # Binary Search solution

    def intersection(self,nums1,nums2):
        sortedArray1 = sorted(nums1)
        sortedArray2 = sorted(nums2)

        i = 0
        j = 0

        output = []

        while i < len(sortedArray1) and j < len(sortedArray2):

            if sortedArray1[i] < sortedArray2[j]:
                i += 1

            elif sortedArray2[j] < sortedArray1[i]:
                j += 1

            else:
                output.append(sortedArray1[i])
                i += 1
                j += 1
        return output

if __name__ == "__main__":

     nums1 = [4,9,5]
     nums2 = [9,4,9,8,4]

     iota = intersection_of_Two_Array()
     ans = iota.intersection(nums1,nums2)

     print(ans)


