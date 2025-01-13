from typing import List


class lemonde_change:


    def change(self,bills:List[int]) -> bool:

        count5,count10 = 0,0
        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            elif bills[i] == 10:
                count10 += 1
                if not count5:
                    return False
                count5 -= 1
            else:
                if count10 and count5:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False
        return True


if __name__ == "__main__":

    lc = lemonde_change()
    bills = [5,5,5,10,20]
    ans = lc.change(bills)
    print(ans)
