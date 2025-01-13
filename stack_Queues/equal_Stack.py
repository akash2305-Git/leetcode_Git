
'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height.
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height.
This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the
same height, then return the height.
'''

class equal_Stack:

    def make_equal_stack(self,h1,h2,h3):
        sum1 = sum(h1)
        sum2 = sum(h2)
        sum3 = sum(h3)

        h1_idx = 0
        h2_idx = 0
        h3_idx = 0

        while not (sum1 == sum2 == sum3):
            if sum1 > sum2 and sum1 > sum3:
                sum1 -= h1[h1_idx]
                h1_idx += 1

            elif sum2 > sum3:
                sum2 -= h2[h2_idx]
                h2_idx += 1

            else:
                sum3 -= h3[h3_idx]
                h3_idx += 1

        return sum1



if __name__ == "__main__":

    es = equal_Stack()

    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]

    ans = es.make_equal_stack(h1,h2,h3)

    print(ans)



