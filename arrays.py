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
    






