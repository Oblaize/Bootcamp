# Bootcamp
Below is the basic code used to generate the prime numbers from 0 to a given number n:

prime_nums = [2]
for i in range(3,n+1):
    # start from 3 onwards
    # "outer loop"
    factor_count=0
    for x in range (2,i):
        # start from 2 onwards
        if i % x == 0:
            factor_count+=1
            # inner loop breaking..
            break # i is not a prime number 
    if factor_count==0:
        prime_nums.append(i)
In the above code, there exists two loops. The outer loop iterates through all the numbers from 3 and n, which gives us n-3.

The inner loop seems to iterate through the numbers 2 up to i-1, which gives us i-3.

However, this doesn't happen if the number is not a prime number, since the loop breaks when one factor is found.

The worst case scenario that would give us the quadractic O(N^2) would therefore mean that all the numbers between 0 and the number n are prime nunmbers, which is not the actual behaviour of numbers. This means that the code runs with more efficiency that O(N^2).

These facts aside, the big-O notation of the above code would be (n-3)(n-1), which approximates to n^2. The Big-O analysis of the above code is therefore quadratic O(N^2).
