# Challenge number 1.
multiples = []

def ch1(x):
    for i in range(x):
        if i % 3 == 0:
            multiples.append(i)
        if i % 5 == 0:
            if i not in multiples:
                multiples.append(i)

    print(multiples)
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

ch2(4000000)


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
# UNFINISHED
palindromes = []
def ch4():
    for i in range(100,1000):
        for j in reversed(range(100,1000)):
            while i != j:
                x = i * j
                print(x)
                



#ch4()
"""digits = [int(a) for a in str(x)]
                if digits == digits.reverse():
                palindromes.append("".join(digits))"""