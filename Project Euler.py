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


# Challenge number 3.
def ch3(x):
    i = 2
    while i * i <= x:
        while x % i == 0:
            x /= i
        i += 1   
    print(int(x))
        
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

#ch4()


# Challenge number 5.
#UNFINISHED
def ch5():
    for i in range(1, 1000000):
        j = 1
        while j <= 20:
            if i % j == 0:
                j += 1
            else:
                continue
            print(i)

ch5()