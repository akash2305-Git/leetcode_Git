class Minimum_count:

    def min_count(self, V, M, coins):
        count = []
        min_count = 0
        i = 0
        j = 0
        while j < M:
            if coins[i] + coins[j] == V:
                return 0




if __name__ == "__main__":
    V = 30
    M = 3
    coins = [25,10,5]

    mc = Minimum_count()
    ans = mc.min_count(V, M, coins)
    print(ans)
