idx = 0
prime = 2
numbers = []

def factor(num: int) -> []:
    global prime
    global idx
    global numbers
    if(prime<=num):
        if(num%prime==0):
            numbers.append(prime)
            factor(num/prime)
        else:
            prime += 1
            factor(num)

    return numbers

print(factor(12))
numbers = []
print(factor(35))
numbers = []






