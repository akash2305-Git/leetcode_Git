

class Prefix_to_Infix:

    def prefixToInfix(self,pre_exp):

        st = []
        ans = ''

        for i in range(len(pre_exp)-1,-1,-1):
            c = pre_exp[i]

            if c.isalpha():
                st.append(c)
            else:
                s1 = st.pop()
                s2 = st.pop()
                res = '('+s1+c+s2+')'
                st.append(res)

            return st[-1]



if __name__ =="__main__":


    pre_exp = '*-A/BC-/AKL'
    PI = Prefix_to_Infix()
    ans = PI.prefixToInfix(pre_exp)
    print(ans)

