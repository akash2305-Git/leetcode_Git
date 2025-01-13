

"""
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Problem Constraints
1 <= |A| <= 106
1 <= Ai <= 109

Example Input
A = [2, 1, 2]

Example Output
2

"""






from collections import Counter
class majority:

    def majority_elem(self,A):

        n = len(A)
        half = n//2
        k = Counter(A)

        for i,j in k.items():
            if j>half:
                return i


if __name__ == "__main__":

    A = [2,1,2]

    mj = majority()
    ans = mj.majority_elem(A)
    print(ans)
