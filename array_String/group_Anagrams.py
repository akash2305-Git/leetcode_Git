from collections import defaultdict


class group_Anagram:

    def classify_anagrams(self,strs:list[str]) -> list[list[str]]:

        anagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)


        return list(anagrams.values())


if __name__ == "__main__":

    strs = ["act","pots","tops","cat","stop","hat"]

    ga = group_Anagram()
    ans = ga.classify_anagrams(strs)
    print(ans)
