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

# Answer is: 233168.
#ch1(1000)


# Challenge number 2.
numbers = [0, 1]
evens = []
def ch2(x):
    while (numbers[-1] + numbers[-2]) < x:
        numbers.append((numbers[-1] + numbers[-2]))
        if (numbers[-1] + numbers[-2]) % 2 == 0:
            evens.append((numbers[-1] + numbers[-2]))
    print(sum(evens))

# Answer is: 4613732
#ch2(4000000)


# Challenge number 3.
def ch3(x):
    i = 2
    while i * i <= x:
        while x % i == 0:
            x /= i
        i += 1
    print(int(x))

# Answer is: 6857.
#ch3(600851475143)

# Challenge number 4.
palindromes = []
def ch4():
    for i in range(100,1000):
        for j in range(100,1000):
            x = str(i * j)
            if len(x) == 6 and x == x[::-1]:
                palindromes.append(x)

    print(max(palindromes))

# Answer is: 906609.
#ch4()

# Challenge number 5.
def ch5():
    num = 2520
    i = 2
    while i <= 20:
        if num % i == 0:
            i += 1
        else:
            num += 2520
            i = 2
    print(num)

# Answer is: 232792560.
#ch5()


# Challenge number 6.
numbers = []
squares = []
def ch6():
    for i in range(1, 101):
        squares.append(i**2)
        numbers.append(i)
    result = sum(numbers)**2 - sum(squares)
    print(result)

# Answer is 25164150.
#ch6()


# Challenge number 7.
primes = []
from datetime import datetime
def ch10():
    startime = datetime.now()
    x = 2
    while len(primes) != 10001:
        for i in range(2, x):
            if x % i == 0:
                 break
        else:
            primes.append(x)
        x += 1
    print(primes[-1])
    print(datetime.now()-startime)

 # Answer is: 104743. 
ch10()