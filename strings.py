from typing import List,Dict
from collections import deque
import random

# | Code             | Meaning                  |
# | ---------------- | ------------------------ |
# | `while stack`    | while stack NOT empty    |
# | `if not stack`   | stack IS empty           |
# | `x in stack`     | check element exists     |
# | `x not in stack` | check element NOT exists |

def largestOddNumber(num):
    i=len(num)-1

    while i>=0:
        if int(num[i]) % 2==1:
            return num[:i+1]
        i-=1
    return ""

def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix= strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix=prefix[:-1]

    return prefix

def isIsomorphic(self, s: str, t: str) -> bool:
    map1={}
    map2={}

    for c1,c2 in zip(s,t):
        if c1 in map1 and map1[c1] != c2:
            return False
        
        if c2 in map2 and map2[c2] != c1:
            return False
        
        map1[c1]=c2
        map2[c2]=c1

    return True   

def rotateString(self, s: str, goal: str) -> bool:
    if len(s)!=len(goal) :
        return False
    
    r=s+s

    if goal in r :
        return True
    
    return False
#def rotateString(self, s: str, goal: str) -> bool:
    #return len(s) == len(goal) and goal in (s + s)

def isAnagram(self, s: str, t: str) -> bool:
    return len(s)==len(t) and sorted(s)==sorted(t)

def frequencySort(self, s: str) -> str:
    freq={}

    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    sorted_chars=sorted(freq,key=freq.get,reverse=True)

    result=""
    for ch in sorted_chars:
        result+=ch*freq[ch]

    return result
    
def maxDepth(self, s: str) -> int:
    count=0
    maxCount=0
    for i in s:
        if i=='(':
            count+=1
            maxCount=max(count,maxCount)
        elif i==')':
            count-=1

    return maxCount

def romanToInt(self, s: str) -> int:
    values={
        'I':1, 'V':5, 'X':10,'L':50, 'C':100, 'D':500,'M':1000
    }

    total=0

    for i in range(len(s)):
        if i+1<len(s) and values[s[i+1]]>values[s[i]]:
            total-=values[s[i]]
        else:
            total+=values[s[i]]
    
    return total

def myAtoi(self, s: str) -> int:
    
    i = 0
    n = len(s)

    while i < n and s[i] == ' ':
        i += 1

    sign = 1
    if i < n and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    num *= sign

    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX

    return num

def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):

            # odd length
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(res):
                    res = s[left:right+1]
                left -= 1
                right += 1

            # even length
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(res):
                    res = s[left:right+1]
                left -= 1
                right += 1

        return res
     
def isValid(self, s: str) -> bool:

    stack=[]
    for char in s:
        if char in "{[(":
            stack.append(char)
        else:
            if not stack:
                return False
            
            top=stack.pop()
            if (
                (char == ')' and top != '(') or
                (char == '}' and top != '{') or
                (char == ']' and top != '[') ):
                return False
            
    return not stack

