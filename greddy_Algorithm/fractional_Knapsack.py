
"""
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here.

Example 1:

Input:
N = 3, W = 50
value[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.000000
Explanation:
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack.


Example 2:

Input:
N = 2, W = 50
value[] = {60,100}
weight[] = {10,20}
Output:
160.000000
Explanation:
Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size N and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.
"""


class Item:

    def __init__(self,value,weight):
        self.value = value
        self.weight = weight



class Fraction_Knapsack:

    def knapsack(self,W,arr,n):

        currValue = 0
        finalValue = 0

        for i in range(n):
            if currValue + arr[i].weight <= W:
                currValue += arr[i].weight
                finalValue += arr[i].value
            else:
                remain = W - currValue
                finalValue += arr[i].value / arr[i].weight * remain
                break


        return finalValue





if __name__ == "__main__":


    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    fk = Fraction_Knapsack()
    ans = fk.knapsack(W,arr,n)
    print(ans)


