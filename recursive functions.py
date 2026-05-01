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
        return(num+sum_digets(n//10)) #the num is the remainder of n/10 so it would get the 3, 2 and 1 of 123 and the // rounds
def product_digets(n):
    if n <10: #if n is less than ten than it would multiply by 0 and it would be 0
        return n
    else:
        num = math.remainder(n,10)
        return(num*product_digets(n//10))

    



def main():
    print(factorial(5))
    print(summation(5))
    print(fibonacci(8))
    print(sum_digets(123))
    print(product_digets(234))
main()