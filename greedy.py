from code import interact
from networkx import reverse


class Solution:
    # meetings = [(end[i], start[i], i + 1) for i in range(len(start))]
    # making tuple from the given list

    def greedy_algorithm_template(inputs):
        # Step 1: Initialize the tracking variables (results, registers, metrics)
        result = []      # Or an integer total like profit, count, etc.
        current_state = initial_value
        
        # Step 2: Sort or organize the data based on your "Greedy Criteria"
        # This is the most critical step. You sort by end time, profit, weights, etc.
        inputs.sort(key=lambda x: x.greedy_property, reverse=True/False)
        
        # Step 3: Iterate through the organized elements
        for item in inputs:
            # Step 4: Check if the current choice is valid/feasible
            if is_feasible(item, current_state):
                # Step 5: Make the local choice and update your state
                result.append(item)
                current_state = update_state(current_state, item)
                
        # Step 6: Return the global optimum reached
        return result

# problems
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        while child_ptr < len(g) and cookie_ptr < len(s):
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1

            cookie_ptr += 1

        return child_ptr
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
                
        return True
    
    def canJump(self, nums: List[int]) -> bool:
        maxlen,leng=0,0

        for i in range(len(nums)):
            if i>maxlen:     # acnt just loop on all
                return False
            
            maxlen=max(maxlen,i+nums[i])

            if maxlen>=len(nums)-1:
                return True
            
        return maxlen>=len(nums)-1

    def jump(self, nums: List[int]) -> int:
        jump,maxlen=0,0
        l,r=0,0

        while r<len(nums)-1:
            for i in range(l,r+1):
                maxlen=max(maxlen,nums[i]+i)
            l=r+1
            r=maxlen
            jump+=1

        return jump

    def maxMeetings(self, start, end):
        # Store as (end, start, index)
        meetings = [(end[i], start[i], i + 1) for i in range(len(start))]

        # Sort primarily by end time
        meetings.sort()
        # meetings.sort(key=lambda x: x[0]) 

        result = []
        last_end = -1

        for e, s, idx in meetings:
            # Fix: Use >= to allow a meeting to start right when the last one ends
            if s >= last_end:  
                result.append(idx)  
                last_end = e  
                
        return result
    
    def countPlatforms(self, arr, dep, n):
        # Create sorted copies so we don't destroy the original input data
        sorted_arr = sorted(arr)
        sorted_dep = sorted(dep)

        # Initialize pointers and counters
        platforms = 1
        result = 1
        i, j = 1, 0

        # Traverse arrival and departure timelines chronologically
        while i < n and j < n:
            # If a train arrives before (or exactly when) another departs, we need a platform
            if sorted_arr[i] <= sorted_dep[j]:
                platforms += 1
                i += 1
            # If a train departs, a platform becomes empty
            else:
                platforms -= 1
                j += 1

            # Keep track of the peak overlapping platforms
            result = max(result, platforms)

        return result

class Job:
    def __init__(self, id, dead, profit):
        self.id=id
        self.dead=dead
        self.profit=profit

        def JobScheduling(arr, n):
            arr.sort(key=lambda x:x.profit,reverse=True)

            maxi=arr[0].dead
            for i in range(1,n):
                maxi=max(maxi,arr[i].dead)

            slot=[-1]*(maxi+1)

            cJob,prof=0,0

            for i in range(n):
                for j in range(arr[i].dead,0,-1):   #Find a slot for the current job, starting from the job's deadline
                    if slot[j]==-1:
                        slot[j]=i
                        prof+=arr[i].profit
                        cJob+=1
                        break

            return cJob,prof

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        count=0
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<end:
                count+=1
            else:
                end=intervals[i][1]

        return count

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
            
    # Crucial Step: Must sort by start time first
    intervals.sort(key=lambda x: x[0])
        
    # Initialize result with the first interval
    res = [intervals[0]]
        
    for i in range(1, len(intervals)):
        # If current interval overlaps with the last added interval
        if intervals[i][0] <= res[-1][1]:
            # Merge them by expanding the end boundary
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            # No overlap, safely append the new isolated interval
            res.append(intervals[i])
            
    return res  

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        
        for i, (s, e) in enumerate(intervals):
            if e < newInterval[0]:
                left.append(intervals[i])
            elif s > newInterval[1]:
                right.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], s), max(newInterval[1], e)]
                
        return left + [newInterval] + right

    # for idx, s, e in [(i, inv[0], inv[1]) for i, inv in enumerate(intervals)]:    i=index and inv=each list inside the list
    # for i, (start, end) in enumerate(intervals):
    # print(f"Interval row {i} runs from {start} to {end}")
    


