
'''
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''

class longest_Palindrome:


    def longest_substring(self,s:str) -> str:
        return 0


    ''' 
    def longest_substring(self,s:str) -> str:
        if len(s) <= 1:
            return s

        Max_len = 1
        Max_str = s[0]

        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_len = j-i+1
                    Max_str = s[i:j+1]

        return Max_str
        
    '''


if __name__ == "__main__":

    lp = longest_Palindrome()
    s = "babad"
    ans = lp.longest_substring(s)

    print("longest palindrome string is:",ans)
