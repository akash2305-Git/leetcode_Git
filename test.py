from collections import defaultdict

strs = ["act", "pots", "tops", "cat", "stop", "hat"]

anagrams = defaultdict(list)
for s in strs:
            # Sort the string to create a key
            key = ''.join(sorted(s))
            anagrams[key].append(s)
print(anagrams.values())
