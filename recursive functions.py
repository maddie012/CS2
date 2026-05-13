#recursive functions
#Author: Madeleine Elias
#description: has a bunch of recursive functions
#sources: google(i had to look up how to round, how to use powers, how to find remainders, what eculidian is, what fibonacci is, ect)
import math
def factorial(n):
    '''description: multiples group of numbers together if put in factorial 4 then it is 4*3*2*1
    args:
        n: any number greater than 1
    returns:
        the factorial of n'''
    if n <= 1:
        return 1
    return( n * factorial(n-1))
def summation(n):
    '''description: finds the summation of a number, it adds all the numbers below it ex: summation 4 is 4+3+2+1
    args:
        n is a number 
    returns:
        the summation of n'''
    if n <= 1:
        return 1
    return(n + summation(n-1))
def exponential(a,b,x):
    '''decriptions: it finds the exponential of a certian value, it uses b and multiples it by a recursive wth x-1 so it will keep multipling until x is 0
    args:
        a, b, x:  these are numbers for the exponential function a(b^x)
    returns:
        the exponential of the equation'''
    if x==0:
        return a
    return(b*exponential(a,b,x-1))
def fibonacci(n):
    '''description: put in a number and find which fibonacci number it is
    args:
        n is which number in the sequence it wants
    returns:
        a fibbonacci number that is n number in the sequence'''
    if n<=2:
        return 1
    return(fibonacci(n-1)+fibonacci(n-2))
def sum_digets(n):
    '''Description: finds the sum of the digets, first it divides it by ten and finds the remainder(whats in the one place), then it adds that to the sumdigets or n/10 but uses // so it will round to a whole number
    args: 
        n: a number that the funcion will get the sum of digits 
    returns:
        the sum of the digits of n'''
    if n == 0:
        return 0
    num = math.remainder(n,10)
    return(num+sum_digets(n//10)) #the // rounds it to the nearest whole number
def product_digets(n):
    '''Description: finds the product of the digets, first it divides it by ten and finds the remainder(whats in the one place), then it multiples that to the productdigets or n/10 but uses // so it will round to a whole number
    args: 
        n: a number that the funcion will get the product of digits 
    returns:
        the product of the digits of n'''
    if n <10: #if n is less than ten than it would multiply by 0 and it would be 0
        return n
    num = math.remainder(n,10)
    return(num*product_digets(n//10))
def two_whole(n,x):
    '''description: finds the product of two whole numbers by adding them certain amount of times (6 groups of 8)
    args:
        n,x: two whole numbers
    returns:
        the product of the two numbers'''
    if n==0 or x==0:
        return 0 
    return(x+two_whole(n-1,x))
def sum_range(s,l):
    '''description: finds the sum of numbers between s and l
    args:
        s: random number smaller than l
        l: random number larger than s
    returns:
        the sum of the numbers between s and l'''
    if s >= (l-1): 
        return 0 
    return((s+1)+sum_range(s+1,l))
def flip(n):
    '''description: it flips a numbers digits around by getting the ones digit then the tens and priting them in another order
    args:
        n: the number they want flipped
    returns:
        the number flipped around'''
    if n<10:
        return n
    num = math.remainder(n,10)
    return(f'{num},{flip(n//10)}')
def eculidean(a,b):
    '''Description: finds the greatest common divisor between a and b
    args:
        a: a number that is bigger than b
        b: a number that is smaller than a
    returns:
        the greatest common divisor between a and b'''
    if b>a:
        eculidean(b,a)
    r = math.remainder(a,b)
    if r==0:
        return b
    return(eculidean(b,r))
def compound_interest(p,r,n,t):
    '''Description: returns the the amount of money they will have after compound interest if when the user puts in the amount and it rounds to 2 decimal places
        (this function does not use recursive functions)
    args:
        p = initial amount
        r = annual rate(decimal)
        n = coumpounding frequency (how many times a year its compounded)
        t = time
    returns:
        the amount of money they will have after calculating interest
    '''
    if  t==0 or n==0:
        return p
    return(round(exponential(p,(1+(r/n)),(n*t)),2))
def bisection(min,max,n):
    e = .05
    y = (min+max)/2
    if abs(y**2 - n)<=e:
        return y
    elif y**2 > n:
        return bisection(min, y, n)
    elif y**2 < n:
        return bisection(y,max,n)
    return(min+max)/2

def main():
    print(factorial(5))
    print(summation(5))
    print(exponential(3,2,4))
    print(fibonacci(8))
    print(sum_digets(123))
    print(product_digets(234))
    print(two_whole(6,8))
    print(sum_range(3,8))
    print(flip(123))
    print(eculidean(270,192))
    print(compound_interest(10000,0.25,12,7))
    print(bisection(0,9,9))
main()