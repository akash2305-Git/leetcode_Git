

class max_score:

    def maxScore(self,s:str) -> int:

        total_one = s.count('1')
        sum_zero = 0
        max_count = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                sum_zero += 1
            else :
                total_one -= 1

            current_score = sum_zero + total_one

            max_count = max(max_count,current_score)

        return max_count



if __name__ == "__main__":

    ms = max_score()

    s = "011101"

    ans = ms.maxScore(s)

    print(ans)
