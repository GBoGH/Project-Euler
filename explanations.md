### Problem number 1.

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
> Find the sum of all the multiples of 3 or 5 below 1000.  
##### The Output is: 233168.

```python
# Challenge number 1.
multiples = []
def ch1(x):
    for i in range(x):
        if i % 3 == 0:
            multiples.append(i)
        if i % 5 == 0:
            if i not in multiples:
                multiples.append(i)
    print(sum(multiples))

ch1(1000)
# Output is: 233168.
```

Function checks whether number in given range is divisble by three ` if i % 3 == 0: `, then it chceck whether the same number is divisible by five `if i % 5 == 0`. As a last step, it chcecks if the number is not already in list multiples `if i not in multiples`. If all three conditions are fulfilled, the number is added to list which is than added together.
  
<br />  
  
### Problem number 2.

> Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms   will be:  
> 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...  
> By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.  
##### The Output is: 4613732

```python
# Challenge number 2.
numbers = [0, 1]
evens = []
def ch2(x):
    while (numbers[-1] + numbers[-2]) < x:
        numbers.append((numbers[-1] + numbers[-2]))
        if (numbers[-1] + numbers[-2]) % 2 == 0:
            evens.append((numbers[-1] + numbers[-2]))
    print(sum(evens))

ch2(4000000)
# Output is: 4613732
```

There are more ways to solve fibonacci number in python, I chose probably the slower one but it is usable in this case as it is not dealing with large numbers. Otherwise regression would be better approach.  
The principle used is that this function adds the last two values in the list numbers `numbers[-1] + numbers[-2]` and adds the sum to the said list as its last value `numbers.append((numbers[-1] + numbers[-2]))`. Then it selects the even numbers from complete list `if (numbers[-1] + numbers[-2]) % 2 == 0:` and adds them to list of even fibonacci numbers `evens.append((numbers[-1] + numbers[-2]))`. Than the function returns sum of values present in the evens list.
  
<br />   
  
### Problem number 3.
> The prime factors of 13195 are 5, 7, 13 and 29.
> What is the largest prime factor of the number 600851475143 ?  
##### The Output is: 6857

```python
# Challenge number 3.
def ch3(x):
    i = 2
    while i * i <= x:
        while x % i == 0:
            x /= i
        i += 1
    print(int(x))

ch3(600851475143)
# Output is: 6857.
```

Every number can have only prime factor which is larger than its square root. Thats why we know it is the largest prime factor. The function is given starting argument i which is 2. 1 would not work because than the inner loop would never break. First while loop is checking wether the square of found number is smaller than x. If it is not we have our largest prime. Inner loop divides x until it gets to prime number. If the inner loop breaks the x in entered in the outer loop which determines if it is the largest prime or not. If the square is larger than the input it is the largest prime factor. If it is not than 1 is added to i and loop continues.
 
 <br />
 
  ### Problem number 4.
> A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
> Find the largest palindrome made from the product of two 3-digit numbers.
##### The answer is: 906609.

```python
# Challenge number 4.
palindromes = []
def ch4():
    for i in range(100,1000):
        for j in range(100,1000):
            x = str(i * j)
            if len(x) == 6 and x == x[::-1]:
                palindromes.append(x)

    print(max(palindromes))

ch4()
# Output is: 906609.
```

Fisrt of all we need to multiply every three digit number `x = str(i * j)`.   
Then this condition `if len(x) == 6 and x == x[::-1]:` only selects numbers that have 6 digits as the largest will be one of them and checks wether the number is a palindrome by reversing the string  `x[::-1]`.If both conditions are fulfilled, number is added to palindromes list. Then function prints the largest one from the palindromes.

<br />

### Problem number 5.
> 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
> What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
##### The answer is: 232792560.

```python
# Challenge number 5.
def ch5():
    num = 2520
    i = 2
    while i != 20:
        if num % i == 0:
            i += 1
        else:
            num += 2520
            i = 2
    print(num)

ch5()
# Output is: 232792560.
```

First we have to determine the starting point. In this case it is 2520 as it is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. Then fucntion loops until i is equal to 20. It divides starting number by current i and determines if modulus is 0 `if num % i == 0`. If it is, one is added to i `i += 1` and loop starts again. If num is not divisible by i with remainder of zero, 2520 is added to num `num += 2520` and i is set to its starting value `i = 2` . We add 2520 to num because any mulitple of 2520 will automatically be a multiple of numbers 1 - 10.

<br />

### Problem number 6.
> The sum of the squares of the first ten natural numbers is,  
> 1<sup>2</sup>+2<sup>2</sup>+...+10<sup>2</sup>=385  
> The square of the sum of the first ten natural numbers is,  
> (1+2+...+10)<sup>2</sup>=55<sup>2</sup>=3025  
> Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.  
> Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
##### The answer is: 25164150.

```python
# Challenge number 6.
numbers = []
squares = []
def ch6():
    for i in range(1, 101):
        squares.append(i**2)
        numbers.append(i)
    result = sum(numbers)**2 - sum(squares)
    print(result)

ch6()
# Output is 25164150.
```

This function is fairly simple. For first one hundred natural numbers `for i in range(1, 101):`, it first squares the number and adds it to squares list `squares.append(i**2)` and then it simply adds the number to numbers list `numbers.append(i)`. As the output, function returns difference between the sums of lists, one of which is squared `result = sum(numbers)**2 - sum(squares)`.

<br />

### Problem number 7.
> By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  
> What is the 10 001st prime number?
##### The answer is 104743.

```python
# Challenge number 7.
primes = []
def ch7():
    x = 2
    while len(primes) != 10001:
        for i in range(2, x):
            if x % i == 0:
                 break
        else:
            primes.append(x)
        x += 1
    print(primes[-1])

ch7()
# Output is: 104743.
```

**This is a _horribly_ slow solution. I am working on another one**  
As I had already mentioned, this is a really slow and ineffective solution. It takes around 80 seconds on my computer. I have seen solutions under a second. Thats why I am working on improving it. Despite being slow as hell, it works so I will explain it anyways.  
