from curses.ascii import isalnum
import math
from typing import List


def countDigits(n):
    if n==0:
        return 1
    count=0
    while n>0:
        count+=1
        n=n//10
    return count

def reverse(self, x: int) -> int:
    neg=x<0
    x=abs(x)
    
    sum=0
    while x>0:
        a=x%10
        sum=sum*10+a
        x=x//10
    ans= -sum if neg else sum

    if ans<-2**31 or ans>2**31-1:
        return 0
    
    return ans

def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False    
    if x < 10:
        return True
    
    b=x
    sum=0
    while b>0:
        a=b%10
        sum=sum*10+a
        b=b//10
    
    return sum==x

def armstrong(x: int) -> bool:
    b = x
    sum_num = 0
    while b > 0:
        a = b % 10
        sum_num += a ** 3  # ** is the exponent operator
        b = b // 10
    return sum_num == x

def is_prime(n: int) -> bool:
    if n<=1:
        return False
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            count+=1
            if(n//i)!=i:
                count+=1
                
    return count==2

def sum_of_divisors(x: int) -> int:
    sum_num = 0
    # range loop is exclusive of the end, so we add +1
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            sum_num += i
            if i != x // i:
                sum_num += x // i
    return sum_num

def sum_of_all_divisors(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += sum_of_divisors(i)
    return total_sum

def sum_of_all_divisors(n: int) -> int:
    total_sum = 0
    
    # Loop through every possible divisor from 1 to n
    for i in range(1, n + 1):
        # i appears (n // i) times as a divisor between 1 and n
        total_sum += i * (n // i)
        
    return total_sum

def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return b if a == 0 else a

def lcm(a: int, b: int) -> None:
    print((a * b) // gcd(a, b))

# recursion basics
def print_nos(n: int) -> None:
    print(n, end=" ")
    if n > 1:
        print_nos(n - 1)

def print_gfg(n: int) -> None:
    if n > 1:
        print_gfg(n - 1)
    print("GFG", end=" ")

def sum_of_series(n: int) -> int:
    if n == 1:
        return 1
    return sum_of_series(n - 1) + (n * n * n)

def factorial_numbers(n: int) -> list:
    result_list = []
    fact = 1
    i = 1
    while fact < n:
        result_list.append(fact)
        i += 1
        fact = fact * i
    return result_list

def fibonacci(N):
    # Base case: if N is 0 or 1, return N
    if N <= 1:
        return N
    else:
        return fibonacci(N-1)+fibonacci(N-2)

def fib(n:int):
    f=[]
    f[0]=0
    f[1]=1
    for i in range(2,n):
        f[i]=f[n-1]+f[n-2]

def swap(a: int, b: int, arr: list) -> None:
    arr[a], arr[b] = arr[b], arr[a]

def reverse_array(arr: list) -> None:
    n = len(arr) - 1
    i = 0
    while i < n - i:
        swap(i, n - i, arr)
        i += 1 

def reverse_range(arr: list, start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def isPalindrome(self, s: str) -> bool:
    r=[]
    for ch in s:
        if ch.isalnum():
            r.append(ch.lower())

    i=0
    n=len(r)-1
    while(i<=n):
        if r[i]!=r[n]:
            return False
        else:
            i+=1
            n-=1
    return True

def largest(arr: list) -> int:
    n = len(arr)
    large = arr[0]
    if n == 1:
        return arr[0]
    for i in range(1, n):
        if arr[i] > large:
            large = arr[i]
    return large

def get_second_largest(arr: list) -> int:
    second_large = -1
    n = len(arr)
    large = arr[0]
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] < large and arr[i] > second_large:
            second_large = arr[i]
    return second_large

def sortedandRotated(nums: list) -> bool:
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]: #Compare with next element in a circular way
            count += 1
        if count > 1:  # More than one break in order means it's not a rotated sorted array
            return False
    return True

def search_in_sorted(arr: list, k: int) -> bool:
    for item in arr:
        if item == k:
            return True
    return False

def removeDuplicates(self, nums) -> int:
        # If list is empty, return 0
        if not nums:
            return 0

        # Pointer for last unique element
        i = 0

        # Traverse list starting from second element
        for j in range(1, len(nums)):
            # If current element is different from last unique one
            if nums[j] != nums[i]:
                # Move pointer forward
                i += 1
                # Place the unique element in next position
                nums[i] = nums[j]

        # i is last index of unique element, count = i + 1
        return i + 1

def rotateArrayByOne(self, nums):
    temp=nums[0]
    n=len(nums)

    for i in range(len(nums)):
        nums[i-1]=nums[i]
    
    nums[n-1]=temp

class Solution:
    # Helper function to reverse part of array between two indices
    def reverse(self, nums, start, end):
        # Swap elements from start to end
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Function to rotate array left or right by k steps
    def rotateArray(self, nums, k, direction):
        # Get length of array
        n = len(nums)

        # Edge case: no rotation needed
        if n == 0 or k == 0:
            return nums

        # Normalize k if it's larger than n
        k = k % n

        # If direction is right
        if direction == "right":
            # Step 1: reverse the entire array
            self.reverse(nums, 0, n - 1)

            # Step 2: reverse first k elements
            self.reverse(nums, 0, k - 1)

            # Step 3: reverse remaining n-k elements
            self.reverse(nums, k, n - 1)

        # If direction is left
        elif direction == "left":
            # Step 1: reverse first k elements
            self.reverse(nums, 0, k - 1)

            # Step 2: reverse remaining n-k elements
            self.reverse(nums, k, n - 1)

            # Step 3: reverse entire array
            self.reverse(nums, 0, n - 1)

        # Return rotated array
        return nums
class rotate:
    def reverse(self, nums, start, end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1

    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        if n == 0 or k == 0:
            return nums
        
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)

def moveZeroes(self, nums):
    # Pointer to the first zero
    j = -1

    # Find the first zero
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break

        # If no zero found, return
    if j == -1:
        return

        # Start from the next index of first zero
    for i in range(j + 1, len(nums)):
        # If current element is non-zero
        if nums[i] != 0:
                # Swap with nums[j]
            nums[i], nums[j] = nums[j], nums[i]
                # Move j to next zero
            j += 1

def move_zeroes(nums: list) -> None:
    j = 0
    i = 0
    while i < len(nums) and j < len(nums):
        if nums[i] != 0:
            swap(i, j, nums)
            j += 1
            i += 1
        else:
            i += 1

def find_union_sorted(a: list, b: list) -> list:
    res = []
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
        # Pick the smaller element to maintain sorted order
        if a[i] < b[j]:
            val = a[i]
            i += 1
        elif b[j] < a[i]:
            val = b[j]
            j += 1
        else:
            val = a[i]
            i += 1
            j += 1
            
        # Avoid duplicates in the result list
        if not res or res[-1] != val:
            res.append(val)
            
    # Append any remaining elements from array a
    while i < len(a):
        if not res or res[-1] != a[i]:
            res.append(a[i])
        i += 1
        
    # Append any remaining elements from array b
    while j < len(b):
        if not res or res[-1] != b[j]:
            res.append(b[j])
        j += 1
        
    return res
    
def findMaxConsecutiveOnes(self, nums):
    count,maxcount=0,0

    for i in range(len(nums)):
        if nums[i]==1:              ## If current element is 1, increment count
            count+=1
        else:
            count=0
            maxcount=max(count,maxcount)

    return maxcount

def getSingleElement(self, arr):
    xorr = 0

        # XOR all elements — duplicates cancel out
    for num in arr:
        xorr ^= num

    return xorr

def single_number(nums: list) -> int:
    hash_map = {}
    for ele in nums:
        hash_map[ele] = hash_map.get(ele, 0) + 1
    for key, val in hash_map.items():
        if val == 1:
            return key
    return -1

def remove_duplicates(nums: list) -> int:
    if len(nums) == 0:
        return 0
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

def two_sum(nums: list, target: int) -> list:
    mapping = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in mapping:
            return [mapping[complement], i]
        mapping[num] = i
    return []

def two_sum_ii(numbers: list, target: int) -> list:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []

def three_sum(nums: list) -> list:
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]: left += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return res

def four_sum(nums: list, target: int) -> list:
    res = []
    if not nums or len(nums) < 4:
        return res
    nums.sort()
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]: continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]: continue
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    return res

#Dutch National Flag
def sort_colors(nums: list) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            swap(low, mid, nums)
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            swap(mid, high, nums)
            high -= 1

#BOYER-MOORE Algo
def majorityElementn2(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        el = 0
        
        # Applying the algorithm
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
        
        """ Checking if the stored element is the majority element"""
        cnt1 = nums.count(el)
        
        # Return element if it is a majority element
        if cnt1 > (n // 2):
            return el
        
        # Return -1 if no such element found
        return -1

def majority_elementn3(nums: list) -> list:
    mapping = {}
    count = len(nums) // 3
    res = []
    for num in nums:
        mapping[num] = mapping.get(num, 0) + 1
        if mapping[num] == count + 1:
            res.append(num)
    return res
#Kadane algo
def maxSubArray(self, nums: List[int]) -> int:
        
        # maximum sum
        maxi = float('-inf') 
        
        # current sum of subarray
        sum = 0 
        
        # Iterate through the array
        for i in range(len(nums)):
            
            # Add current element to the sum
            sum += nums[i] 
            
            # Update maxi if current sum is greater
            if sum > maxi:
                maxi = sum 
            
            # Reset sum to 0 if it becomes negative
            if sum < 0:
                sum = 0 
        
        return maxi

def stockbuySell(self, prices):
        # Initialize the minimum price to a large number
        min_price = float('inf')

        # Initialize the maximum profit to 0
        max_profit = 0

        # Traverse each price in the array
        for price in prices:
            # If current price is less than min_price, update min_price
            if price < min_price:
                min_price = price
            # Else calculate profit and update max_profit if it's greater
            else:
                max_profit = max(max_profit, price - min_price)

        # Return the maximum profit found
        return max_profit

def rearrange_by_sign(self, A) -> List[int]:
        n = len(A)
        ans = [0] * n  # Initialize result array with zeros

        pos_index = 0  # Even indices for positive numbers
        neg_index = 1  # Odd indices for negative numbers

        for i in range(n):
            if A[i] < 0:
                # Place negative at odd index
                ans[neg_index] = A[i]
                neg_index += 2
            else:
                # Place positive at even index
                ans[pos_index] = A[i]
                pos_index += 2

        return ans

def next_permutation(nums: list) -> None:
    ind = -1
    n = len(nums)
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break
    if ind != -1:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                swap(i, ind, nums)
                break
    reverse_range(nums, ind + 1, n - 1)

def leaders(self, nums):
        ans = []
        
        if not nums:
            return ans
        
        # Last element of the list is always a leader
        max_val = nums[-1]
        ans.append(nums[-1])
        
        # Check elements from right to left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_val:
                ans.append(nums[i])
                max_val = nums[i]
        
        '''Reverse the list to match the required output order'''
        ans.reverse()
        
        # Return the leaders
        return ans

def longestConsecutive(self, nums):
        n = len(nums)
        # If the array is empty
        if n == 0:
            return 0 

        # Initialize the longest sequence length
        longest = 1 
        st = set()

        # Put all the array elements into the set
        for i in range(n):
            st.add(nums[i])

        # Traverse the set to find the longest sequence
        for it in st:
            # Check if 'it' is a starting number of a sequence
            if it - 1 not in st:
                # Initialize the count of the current sequence
                cnt = 1 
                # Starting element of the sequence
                x = it 

                # Find consecutive numbers in the set
                while x + 1 in st:
                    # Move to the next element in the sequence
                    x = x + 1 
                    # Increment the count of the sequence
                    cnt = cnt + 1 
                # Update the longest sequence length
                longest = max(longest, cnt)
        return longest

def spiral_order(matrix: list[list[int]]) -> list:
    r, c = len(matrix), len(matrix[0])
    left, right = 0, c - 1
    top, bottom = 0, r - 1
    res = []
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res

def rotateClockwise(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap element at (i, j) with (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            # Reverse the current row to simulate clockwise rotation
            matrix[i].reverse()

def longest_subarray(arr: list, k: int) -> int:
    max_len = 0
    current_sum = 0
    sum_map = {}
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == k:
            max_len = max(max_len, i + 1)
        rem = current_sum - k
        if rem in sum_map:
            length = i - sum_map[rem]
            max_len = max(max_len, length)
        if current_sum not in sum_map:
            sum_map[current_sum] = i
    return max_len

def max_sub_array(nums: list) -> int:
    curr = max_val = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        max_val = max(max_val, curr)
    return max_val

def find_subarray(arr: list) -> list:
    current_sum = 0
    max_sum = -float('inf')
    start = 0
    ans_start = ans_end = -1
    for i in range(len(arr)):
        if arr[i] >= 0:
            current_sum += arr[i]
            if current_sum > max_sum or (current_sum == max_sum and (i - start > ans_end - ans_start)):
                max_sum = current_sum
                ans_start = start
                ans_end = i
            if current_sum < 0:
                current_sum = 0
        else:
            current_sum = 0
            start = i + 1
            
    if ans_start == -1:
        return [-1]
        
    return arr[ans_start:ans_end + 1] # Python slicing syntax

def max_subarray_sum_circular(nums: list) -> int:
    min_curr = min_val = max_curr = max_val = total = nums[0]
    for i in range(1, len(nums)):
        min_curr = min(nums[i], nums[i] + min_curr)
        min_val = min(min_val, min_curr)
        max_curr = max(nums[i], nums[i] + max_curr)
        max_val = max(max_val, max_curr)
        total += nums[i]
        
    if max_val < 0:
        return max_val
    return max(max_val, total - min_val)

def max_product(nums: list) -> int:
    min_val = max_val = ans = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            min_val, max_val = max_val, min_val  # elegant swap trick
        min_val = min(nums[i], min_val * nums[i])
        max_val = max(nums[i], max_val * nums[i])
        ans = max(ans, max_val)
    return ans

def subarray_sum(nums: list, k: int) -> int:
    mapping = {0: 1}
    pre_sum = count = 0
    for ele in nums:
        pre_sum += ele
        rem = pre_sum - k
        count += mapping.get(rem, 0)
        mapping[pre_sum] = mapping.get(pre_sum, 0) + 1
    return count

def genrow(row: int) -> list:
    ans = 1
    ans_row = [1]
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ans_row.append(ans)
    return ans_row

def generate_pascal(num_rows: int) -> list[list[int]]:
    ans = []
    for i in range(1, num_rows + 1):
        ans.append(genrow(i))
    return ans

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])  # equivalent to custom comparator lambdas in Java
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def merge_sorted_arrays(nums1: list, m: int, nums2: list, n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

def find_missing_repeating_numbers(nums: list) -> list:
    i, n = 0, len(nums)
    while i < n:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for index in range(n):
        if nums[index] != index + 1:
            return [nums[index], index + 1]
    return [-1, -1]

class InversionCount:
    def number_of_inversions(self, nums: list) -> int:
        return self._merge_sort(nums, 0, len(nums) - 1)

    def _merge_sort(self, arr: list, left: int, right: int) -> int:
        count = 0
        if left < right:
            mid = left + (right - left) // 2
            count += self._merge_sort(arr, left, mid)
            count += self._merge_sort(arr, mid + 1, right)
            count += self._merge(arr, left, mid, right)
        return count

    def _merge(self, arr: list, left: int, mid: int, right: int) -> int:
        temp = [0] * (right - left + 1)
        i, j, k = left, mid + 1, 0
        inversions = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                inversions += (mid - i + 1)
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for p in range(len(temp)):
            arr[left + p] = temp[p]
        return inversions

def unique_paths(m: int, n: int) -> int:
    N = m + n - 2
    r = m - 1
    res = 1
    for i in range(1, r + 1):
        res = res * (N - r + i) // i
    return res

def length_of_longest_substring(s: str) -> int:
    if len(s) == 0: return 0
    mapping = {}
    max_len = left = 0
    for right in range(len(s)):
        c = s[right]
        if c in mapping and mapping[c] >= left:
            left = mapping[c] + 1
        mapping[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len

def max_meetings(start: list, end: list) -> list:
    meetings = []
    for i in range(len(start)):
        meetings.append([end[i], start[i], i + 1])
    meetings.sort(key=lambda x: x[0])
    result = []
    last_end = -1
    for m in meetings:
        if m[1] > last_end:
            result.append(m[2])
            last_end = m[0]
    return result

def count_platforms(n: int, arr: list, dep: list) -> int:
    arr.sort()
    dep.sort()
    platforms = result = 1
    i, j = 1, 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        result = max(result, platforms)
    return result

def matrix_sum(nums: list[list[int]]) -> int:
    for row in nums:
        row.sort()
    ans = 0
    for col in range(len(nums[0]) - 1, -1, -1):
        max_val = 0
        for row in range(len(nums)):
            max_val = max(max_val, nums[row][col])
        ans += max_val
    return ans












