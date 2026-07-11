import math


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

def fibonacci(N):
    # Base case: if N is 0 or 1, return N
    if N <= 1:
        return N

    # Recursive calls: calculate previous two terms
    last = fibonacci(N - 1)   # (N-1)th term
    slast = fibonacci(N - 2)  # (N-2)th term

    return last + slast

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

