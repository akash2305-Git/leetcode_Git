

'''
Kth largest/smallest element in an array

Problem Statement: Given an unsorted array, print Kth Largest and Smallest Element from an unsorted array.

Examples:

Example 1:
Input: Array = [1,2,6,4,5,3] , K = 3
Output: kth largest element = 4, kth smallest element = 3

Example 2:
Input: Array = [1,2,6,4,5] , k = 3
Output : kth largest element = 4,  kth smallest element = 4
'''

import heapq

class kth_smallest_laegest:

    def kth_largest_maxHeap(self,arr,k):
        pq = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(pq,-arr[i])

        f = k-1
        while f>0:
            heapq.heappop(pq)
            f -= 1

        print("Kth Largest Element is:",-pq[0])

    def kth_smallest_maxHeap(self,arr,k):
        pq = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(pq,arr[i])

        f = k-1
        while f>0:
            heapq.heappop(pq)
            f -= 1

        print("Kth Smallest Element is:",pq[0])





if __name__ == "__main__":

    arr = [1,2,6,4,5,3]
    k = 3

    ksl = kth_smallest_laegest()
    ksl.kth_largest_maxHeap(arr,k)
    ksl.kth_smallest_maxHeap(arr,k)
