

'''
Given two strings s1 and s2, return true if s2 contains a
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
from collections import Counter


class permutation:

    def permutation_string(self,s1:str,s2:str) -> bool:

        L , l = len(s1)-1 , 0
        cnt1 , cnt2 = Counter(s1) , Counter(s2[:L])

        for r,c in enumerate(s2[L:]):
            cnt2[c] += 1
            if cnt1 == cnt2:
                return True
            cnt2[s2[l]] -= 1
            l += 1

        return False



if __name__ == "__main__":

    s1 = "ab"
    s2 = "eidbaooo"

    pr = permutation()
    ans = pr.permutation_string(s1,s2)

    print(ans)
