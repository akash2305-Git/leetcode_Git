from collections import defaultdict


#
# You are given a string s and an integer k. You can choose any character of the string and change it to any
# other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.




class longest_Repeating_character_Replacement:

    def longest_character(self,s,k):

        '''
        n = len(s)-1
        count = 0
        max_count = 0
        for i in range(0,n):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    count += 1
                elif s[i] != s[j]:
                    if k == 0:
                        max_count = max(count,max_count)
                        break
                    else:
                        k -= 1
                        count += 1

        return max_count '''


        '''Solution 1'''
        freqDict = defaultdict(int)
        maxFreq = 0
        maxLength = 0
        start = end = 0
        while end < len(s):
            freqDict[s[end]] += 1

            # maxFreq may be invalid at some points, but this doesn't matter
            # maxFreq will only store the maxFreq reached till now
            maxFreq = max(maxFreq, freqDict[s[end]])

            # maintain the substring length and slide the window if the substring is invalid
            if ((end-start+1) - maxFreq) > k:
                freqDict[s[start]] -= 1
                start += 1
            else:
                maxLength = max(maxLength, end-start+1)
            end += 1
        return maxLength

        '''Solution 2'''

        maxlen, largestCount = 0, 0
        arr = collections.Counter()
        for idx in xrange(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen

        '''solution 3'''
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):

            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1

            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)

            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1

        return longest_str_len

if __name__ == "__main__":

    s = "AABABBA"
    k = 1

    lrcr = longest_Repeating_character_Replacement()

    ans = lrcr.longest_character(s,k)

    print(ans)
