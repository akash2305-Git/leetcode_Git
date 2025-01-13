
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""




class Generate_Parentheses:


    def generate_parentheses_recursion(self,n):

        sol = []
        ans = []

        def backtrack(n_open,n_close):

            if n_open == n_close == n:
                ans.append(''.join(sol))
                return

            if n_open < n:
                sol.append('(')
                backtrack(n_open+1,n_close)
                sol.pop()

            if n_close < n_open :
                sol.append(')')
                backtrack(n_open,n_close+1)
                sol.pop()

        backtrack(0,0)

        return ans




if __name__ == "__main__":

    n = 5
    gp = Generate_Parentheses()

    ans = gp.generate_parentheses_recursion(n)
    print(ans)

