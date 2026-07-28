# stacks n queues
from collections import deque

from arrays import List


class Node:
    def __init__(self,val):
        self.val=val
        self.next= None

class QueuesUsingLL:
    def __init__(self):
        self.size=0
        self.start=None
        self.end=None

    def push(self,x):
        ele=Node(x)
        if self.size==0:
            self.start=ele
            self.end=ele
        else:
            self.end.next=ele
            self.end=ele

        self.size+=1

    def pop(self):
        if self.start is None:
            return -1
        
        value=self.start.val
        temp = self.start
        self.start=temp.next
        del temp
        self.size-=1

        return value
    
    def peek(self):
        if self.start is None:
            return -1
        
        return self.start.val

class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        self.q.reverse()

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
    
    def empty(self) -> bool:
        return len(self.q)==0
        
class MyQueue:
    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]
    

    def empty(self) -> bool:
        return not self.output and self.input

class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
class Game:
    comp=random.choice([1,0,-1])
    input=input("enter yor sign ")

        # -1=snake  1=water 0=gun
    rules={-1:'snake' , 1:'water' , 0:'gun'}
    print(f"you chose {rules[input]} and computer chose {rules[comp]}")

    if comp==-1 and input==1:
        print('you lose')
    elif comp==-1 and input==0:
        print ('you win')
    elif comp==-1 and input==-1:
        print('draw')
    elif comp==1 and input==1:
        print('draw')
    elif comp==1 and input==0:
        print ('you lose')
    elif comp==1 and input==-1:
        print('you win')
    elif comp==0 and input==1:
        print('you win')
    elif comp==0 and input==0:
        print ('draw')
    elif comp==0 and input==-1:
        print('you lose')
    else:
        print("invalid input")

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    map={}
    stack=[]

    for ch in nums2:
        while stack and ch>stack[-1]:
            map[stack.pop()]=ch
        stack.append(ch)

    for num in stack:
        map[num]=-1

    return [map[ch] for ch in nums1]

def nextGreaterEle(self,nums: List[int]) -> List[int]:
    res=[-1]*len(nums)
    stack=[]

    for i in range(len(nums)-1,-1,-1):
        while stack and stack[-1]<nums[i]:
            stack.pop()
        
        if not stack:
            res[i]=-1
        else:
            res[i]=stack[-1]

        stack.append(nums[i])
    
    return res
        
def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n=len(nums)
    res=[]
    stack=[]

    for i in range(2*n-1,-1,-1):
        while stack and stack[-1]<=nums[i%n]:
            stack.pop()

        if i<n:
            res[i]= -1 if not stack else stack[-1]
        
        stack.append(nums[i%n])

    return res

def nextSmallerElement(self, arr):
    n=len(arr)
    res=[-1]*n
    stack=[]

    for i in range(n-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()

        res[i]= -1 if not stack else stack[-1]

        stack.append(arr[i])

    return res

def prevGreaterElement(self, arr):
    n= len(arr)
    res=[-1]*n
    stack=[]

    for i in range(0,n):
        while stack and stack[-1]<=arr[i]:
            stack.pop()

        res[i]=-1 if not stack else stack[-1]

        stack.append(arr[i])

    return res

def prevLesserElement(self, arr):
    n= len(arr)
    res=[-1]*n
    stack=[]

    for i in range(0,n):
        while stack and stack[-1]>=arr[i]:
            stack.pop()

        res[i]=-1 if not stack else stack[-1]

        stack.append(arr[i])

    return res

def sumSubarrayMins(self, arr: List[int]) -> int:
    def psee (self,arr):
        res=[0]* len(arr)
        stack=[]

        for i in range(0,len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()

            res[i]=-1 if not stack else stack[-1]
            stack.append(i)

        return res

    def nse(self,arr):
        stack=[]
        res=[0]*len(arr)

        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()

            res[i]=len(arr) if not stack else stack[-1]
            # we need to store len of the array bc -1 will make it negative on right
            stack.append(i)

        return res

    psee= psee(arr)
    nse= nse(arr)
    total=0
    MOD=10**9+7

    for i in range(0,len(arr)):
        left = i-psee[i]
        right=nse[i]-i

        count = (left*right*arr[i]) % MOD

        total = (total+count) % MOD

    return total % MOD

def sumSubarrayMaxs(self, arr: List[int]) -> int:
    def pgee( self, arr):
        n= len(arr)
        stack=[]
        res=[0]*n

        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()

            res[i]= -1 if not stack else stack[-1]
            stack.append(i)

        return res
    
    def nge( self, arr):
        n= len(arr)
        stack=[]
        res=[n]*n

        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()

            res[i]= n if not stack else stack[-1]
            stack.append(i)

        return res

    total =0
    pgee= pgee(arr)
    nge= nge(arr)
    MOD=10**9+7

    for i in range(0,len(arr)):
        left = i-pgee[i]
        right=nge[i]-i

        count = (left*right*arr[i]) % MOD

        total = (total+count) % MOD

    return total % MOD

def subArrayRanges(self, nums: List[int]) -> int:
    # sumsubarry max-sum subarray min = ans
    total =0
    
    largest=self.sumSubarrayMaxs(nums)
    smallest=self.sumSubarrayMins(nums)
    total = largest-smallest

    return total

def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack=[]
    res=[]
    n= len(asteroids)

    for i in range(n):
        if asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                stack.pop()
            
            if stack and stack[-1]==abs(asteroids[i]):
                stack.pop()
            elif stack and stack[-1]>abs(asteroids[i]):
                continue
            else:
                stack.append(asteroids[i])

    return stack

def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        n= len(num)
        res=""

        if k==n: return '0'

        for ch in num:
            while stack and stack[-1]>ch and k>0:
                stack.pop()
                k-=1

            stack.append(ch)

        if k!=0:
            while k>0:
                stack.pop()
                k-=1

        res="".join(stack)
        res = res.lstrip('0')

        return res if res else "0"

def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water

def trapOtherSoln(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        lmax, rmax = 0, 0
        ans = 0

        while l < r:
            if h[l] < h[r]:
                # Right boundary is taller, so h[l] is the bottleneck
                lmax = max(lmax, h[l])
                ans += lmax - h[l]
                l += 1
            else:
                # Left boundary is taller (or equal), so h[r] is the bottleneck
                rmax = max(rmax, h[r])
                ans += rmax - h[r]
                r -= 1

        return ans

def largestRectangleArea(self, heights: List[int]) -> int:
    stack=[]
    maxx=0
    n= len(heights)
    
    for i in range(n):
        while stack and heights[i]<heights[stack[-1]]:
            h = heights[stack.pop()]
            w=i if not stack else i-stack[-1]-1
            maxx=max(maxx,h*w)

        stack.append(i)
    
    return maxx

    # nse =prevGreaterElement(heights)
    # pse=prevLesserElement(heights)
    # maxA = 0
    # for i in range(len(heights)):
    #     maxA=max(maxA , heights[i] * (nse[i]-pse[i]-1))
    # return maxA

def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix: return 0

    col=len(matrix[0])
    heights=[0]*col
    max_rect=0
    heights.append(0)

    for row in matrix:
        for i in range(col):
            if row[i]=='1':
                heights[i]+=1
            else:
                heights[i]=0

        max_rect=max(max_rect,largestRectangleArea(heights))
    heights.pop()
    return max_rect

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack=[]
    n=len(temperatures)
    answer=[0]*n

    for i in range(len(temperatures)):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            index=stack.pop()
            answer[index]=i-index
        stack.append(i)

    return answer
        
class StockSpanner:

    def __init__(self):
        self.stack=[]   #it will have (price,span) pairs
        
    def next(self, price: int) -> int:
        span=1

        while self.stack and self.stack[-1][0] <= price:  #price at the top of the stack is less then the given price
            span+= self.stack.pop()[1] 

        self.stack.append((price,span))
        return span
    
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    dq= deque()
    res=[]

    for i in range(len(nums)):
        if dq and dq[0]<=i-k:   #to move the window n remove the bottom on
            dq.popleft()

        while dq and nums[dq[-1]]<nums[i]:
            dq.pop()         # to remove the smaler one in stack n add bigger

        dq.append(i)

        if i>=k-1:
            res.append(nums[dq[0]])

    return res

def celebrity(self, M):
    top, bottom= 0, len(M)-1
    celeb=0
    n=len(M)

    while top<bottom:
        if M[top][bottom] == 1:     #top knows bottom
            top+=1
        elif M[bottom][top] == 1:     #bottom knows top
            bottom -=1
        else:        #both know each other
            top+=1
            bottom-=1

    if top>bottom :     #no celebs pointers crossed each other
        return -1

    for i in range(n):      #top==bottom
        if (i==top):         #[0][0]  diagonal elements
            continue

        if M[top][i]==0 and M[i][top]==1:
            return i
        else:
            return -1

        
    return top


