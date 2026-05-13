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
        
        max_len = max(max_len, r - l + 1)

    return max_len

def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def atmost(arr ,goal):
        if goal<0:
            return 0
        
        l,sum,count=0,0,0
        
        for r in range(len(arr)):
            sum+=arr[r]

            while sum>goal:
                sum-=arr[l]
                l+=1

            count+=(r-l+1)  #add length bc we use it in [0,0,0]
        return count

    return atmost(nums,goal)-atmost(nums,goal-1)

def numSubarraysWithSum2(self, nums: List[int], goal: int) -> int:
    counts = {0: 1} # {PrefixSum: Frequency}
    current_sum = 0
    total = 0
    
    for x in nums:
        current_sum += x
        # If (current_sum - goal) exists, it means we found subarrays
        total += counts.get(current_sum - goal, 0)
        counts[current_sum] = counts.get(current_sum, 0) + 1
        
    return total

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def atmost(nums,k):    
        l,count,total=0,0,0

        for r in range(len(nums)):
            if nums[r]%2!=0:
                count+=1
            
            while count>k:
                if nums[l]%2 !=0:
                    count-=1
                l+=1

            total+=(r-l+1)
        return total
    
    return atmost(nums,k) - atmost(nums,k-1)

def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        counts = {0: 1} # {OddCountPrefix: Frequency}
        current_odd_count = 0
        total = 0
        
        for x in nums:
            # Treat every odd number as a 1
            if x % 2 == 1:
                current_odd_count += 1

            # Check if we have seen a prefix that makes the current window have exactly k odds
            total += counts.get(current_odd_count - k, 0)
            
            # Update the frequency of the current prefix count
            counts[current_odd_count] = counts.get(current_odd_count, 0) + 1
            
        return total

def numberOfSubstrings(self, s: str) -> int:
    lastseen={'a':-1,'b':-1,'c':-1}
    count=0

    for i in range(len(s)):
        lastseen[s[i]]=i
        if lastseen['a']!=-1 and lastseen['b']!=-1 and lastseen['c']!=-1:
            count+= 1+min(lastseen['a'],lastseen['b'],lastseen['c'])

    return count

def maxScore(self, cardPoints: List[int], k: int) -> int:
    if len(cardPoints)==k:
        return sum(cardPoints)
    
    lsum,rsum,maxsum=0,0,0

    for r in range(len(cardPoints)):
        