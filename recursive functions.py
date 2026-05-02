#recursive functions
import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return( n * factorial(n-1))
def summation(n):
    if n <= 1:
        return 1
    else:
        return(n + summation(n-1))
def fibonacci(n):
    if n<=2:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
def sum_digets(n):
    if n == 0:
        return 0
    else:
        num = math.remainder(n,10)
        return(num+sum_digets(n/10)) #the num is the remainder of n/10 so it would get the 3, 2 and 1 of 123 but the answer is a bit off because the / does not round
def product_digets(n):
    if n <10: #if n is less than ten than it would multiply by 0 and it would be 0
        return n
    else:
        num = math.remainder(n,10)
        return(num*product_digets(n/10))
def two_whole(n,x):
    if n==0 or x==0:
        return 0 
    else:
        return(x*n)
def sum_range(s,l):
    if s >= (l-1): #l-1 because then it will include l is in the range even though it shouldn't be included, just gets what is between the who numbers
        return 0 
    else:
        return((s+1)+sum_range(s+1,l))
    



def main():
    print(factorial(5))
    print(summation(5))
    print(fibonacci(8))
    print(sum_digets(123))
    print(product_digets(234))
    print(two_whole(6,8))
    print(sum_range(3,8))
main()