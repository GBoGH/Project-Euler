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
        for j in reversed(range(100,1000)):
            while i != j:
                x = i * j
                print(x)

                

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

ch5()
