
"""
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

"""

solution 1:
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindro = []
        path = []
        self.helper(0, s, path, palindro)
        return palindro

    def helper(self, index, s, path, palindro):
        if index == len(s):
            palindro.append(path[:])
            return
        for i in range(index, len(s)):
            if self.is_palindro(s, index, i):
                path.append(s[index:i+1])
                self.helper(i+1, s, path, palindro)
                path.pop()

    def is_palindro(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        
        

"""


class Palindrome_Partition:



    def recursion_partition(self, s):
        lst = []
        def palindrome(a):
            a == a[::-1]

        def dfs(i,curr):
            if i == len(s):
                lst.append(curr)
                return
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(s):
                    dfs(j+1,s+[sol])
            return

        dfs(0,[])
        return lst


if __name__ == "__main__":

    s = "aab"
    pp = Palindrome_Partition()
    ans = pp.recursion_partition(s)
    print(ans)
