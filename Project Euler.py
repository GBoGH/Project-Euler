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

#ch1(1000)
# Output is: 233168.


# Challenge number 2.
numbers = [0, 1]
evens = []
def ch2(x):
    while (numbers[-1] + numbers[-2]) < x:
        numbers.append((numbers[-1] + numbers[-2]))
        if (numbers[-1] + numbers[-2]) % 2 == 0:
            evens.append((numbers[-1] + numbers[-2]))
    print(sum(evens))

#ch2(4000000)
# Output is: 4613732


# Challenge number 3.
def ch3(x):
    i = 2
    while i * i <= x:
        while x % i == 0:
            x /= i
        i += 1
    print(int(x))

#ch3(600851475143)
# Output is: 6857.


# Challenge number 4.
palindromes = []
def ch4():
    for i in range(100,1000):
        for j in range(100,1000):
            x = str(i * j)
            if len(x) == 6 and x == x[::-1]:
                palindromes.append(x)

    print(max(palindromes))

#ch4()
# Output is: 906609.


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

#ch5()
# Output is: 232792560.


# Challenge number 6.
numbers = []
squares = []
def ch6():
    for i in range(1, 101):
        squares.append(i**2)
        numbers.append(i)
    result = sum(numbers)**2 - sum(squares)
    print(result)

#ch6()
# Output is 25164150.


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

#ch7()
# Output is: 104743.

# Challenge number 8.
number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

def ch8():
    ""

#ch8()