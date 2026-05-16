from typing import List


def BSsearch(self, nums: List[int], target: int) -> int:
    l,h=0,len(nums)-1
    while l<=h:
        m=(l+h)//2     #for integer division

        if nums[m]==target:
            return m
        elif nums[m]<target:
            l=m+1
        else:
            r=m-1
    
    return -1

class RotatedArray:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            
            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                # Check if target lies within the sorted left half
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
                    
        return -1

    def searchDuplicates(self, nums: List[int], target: int) -> bool:
        l, h = 0, len(nums) - 1
        
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return True
            
            # CRITICAL DUPLICATE CHECK: Shrink boundaries if ends match the middle
            if nums[l] == nums[m] == nums[h]:
                l += 1
                h -= 1
                continue
                
            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            # Otherwise, the right half is sorted
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
                    
        return False

def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge cases: Array of length 1 or peak at boundaries
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
            
        # Shrink boundaries to avoid index out of bounds checks
        l, h = 1, n - 2
        
        while l <= h:
            m = (l + h) // 2
            
            # If m is greater than both neighbors, it's a peak
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
                
            # If the right neighbor is greater, a peak must exist on the right side
            elif nums[m] < nums[m + 1]:
                l = m + 1
            # If the left neighbor is greater, a peak must exist on the left side
            else:
                h = m - 1
                
        return -1

