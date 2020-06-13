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

# Answer is: 233168.
ch1(1000)
```

