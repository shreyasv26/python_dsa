from typing import List


def lengthOfLongestSubstring(self, s: str) -> int:

    chars = set()

    left = 0
    longest = 0

    for right in range(len(s)):

        # duplicate found
        while s[right] in chars:
            chars.remove(s[left])
            left += 1

        chars.add(s[right])

        longest = max(longest, right - left + 1)

    return longest

def longestOnes(self, nums: List[int], k: int) -> int:
    l,zeros,maxlen=0,0,0

    for r in range(len(nums)):
        if nums[r]==0:
            zeros+=1

        while zeros>k:
            if nums[l]==0:
                zeros-=1
                
            l+=1

        maxlen= max( maxlen, l-r+1)

    return maxlen

def totalFruit(self, fruits: List[int]) -> int:
    l, max_fruits=0,0
    baskets={}

    for r in range(len(fruits)):
        baskets[fruits[r]]=baskets.get(fruits[r],0)+1 
        # if the fruit isnt in the basket keep it as default 0 and add 1 to it else just keeep the no of fruts n increment it

        while len(baskets)>2:
            baskets[fruits[l]]-=1  #reduce the fruit from left count

            if baskets[fruits[l]]==0:
                del baskets[fruits[l]]
            l+=1

        max_fruits=max(max_fruits,r-l+1)

    return max_fruits

def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    max_len = 0
    counts = {} # Dictionary to store {character: frequency}
    max_freq = 0

    for r in range(len(s)):
        # 1. Update the count of the current character
        counts[s[r]] = counts.get(s[r], 0) + 1
        
        # 2. Keep track of the most frequent character in the current window
        max_freq = max(max_freq, counts[s[r]])

        # 3. Check if the window is invalid
        # (Length - max_freq) gives the number of characters to be replaced
        while (r - l + 1) - max_freq > k:
            counts[s[l]] -= 1
            l += 1
        
        # 4. Update the global maximum length
        max_len = max(max_len, r - l + 1)

    return max_len

    
