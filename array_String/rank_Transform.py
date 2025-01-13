from typing import List


class rank_Transform:


    def ranKTransformArray(self,arr:List[int]):

        # rank_list = []
        # digit = 0
        # rank = {}
        #
        # for num in arr:
        #     if num >= digit:
        #         rank[num] = 1
        # for i in range(0,len(arr)-1):
        #     if arr[i] == rank.get(i):
        #         rank_list[i] = i
        #
        # return rank_list

        value_to_rank = []
        sorted_unique_numbers = sorted(list(set(arr)))

        for index in range(len(sorted_unique_numbers)):

            value_to_rank[sorted_unique_numbers[index]] = index + 1

        for index in range(len(arr)):

            arr[index] = value_to_rank[arr[index]]

        return arr

if __name__ == "__main__":

    arr = [40,10,20,30]

    arr1 = [37,12,28,9,100,56,80,5,12]

    rt = rank_Transform()
    ans = rt.ranKTransformArray(arr1)

    print(ans)

