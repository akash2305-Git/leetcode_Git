

'''
Given two sorted arrays arr1 and arr2 and an element k. The task is to find the element that would be at the kth position
of the combined sorted array.

Examples :

Input: k = 5, arr1[] = [2, 3, 6, 7, 9], arr2[] = [1, 4, 8, 10]
Output: 6
Explanation: The final combined sorted array would be - 1, 2, 3, 4, 6, 7, 8, 9, 10. The 5th element of this array is 6.
Input: k = 7, arr1[] = [100, 112, 256, 349, 770], arr2[] = [72, 86, 113, 119, 265, 445, 892]
Output: 256
Explanation: Combined sorted array is - 72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892. 7th element of this array is 256.
'''

class kth_Element:


    def two_array_element(self,k,arr1,arr2):


        n,m = len(arr1),len(arr2)

        if n > m:
            return self.two_array_element(k,arr2,arr1)

        low,high = max(0,k-m),min(k,n)

        while low <= high:

            cut1 = (low+high)//2
            cut2 = k - cut1

            left1 = arr1[cut1-1] if cut1 > 0 else float('-inf')
            left2 = arr2[cut2-1] if cut2 > 0 else float('-inf')

            right1 = arr1[cut1] if cut1 < n else float('inf')
            right2 = arr2[cut2] if cut2 < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                return max(left1,left2)
            elif left1 > right2:
                high = cut1 - 1
            else :
                low = cut1 + 1



if __name__ == "__main__":

    ke = kth_Element()
    k = 5
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    ans = ke.two_array_element(k,arr1,arr2)
    print("The kth position element is",ans)
