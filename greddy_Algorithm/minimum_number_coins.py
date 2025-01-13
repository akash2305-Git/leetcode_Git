

'''
Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
'''



class minimum_number_coin:

    def minimum_coin(self,ans,m,v):

        ans = []

        for i in range(0,m):

            while v >= coins[i]:
                v -= coins[i]
                ans.append(coins[i])
        return len(ans)




if __name__ == "__main__":

    mnc = minimum_number_coin()
    coins = [25, 10, 5]
    m = len(coins)
    v = 30
    ans = mnc.minimum_coin(coins,m,v)
    print("Minimum Number of Coin Required is",ans)


