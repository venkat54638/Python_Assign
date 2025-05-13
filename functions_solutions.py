# Easy functions Assignment
# First function
def Calculate_average(num):
    if not num:
        return 0
    return sum(num) / len(num)
# Test cases
print(Calculate_average([5, 10, 15, 20]))
print(Calculate_average([]))

# Second function
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"
    
# Test cases
print(greet_user("Alice"))
print(greet_user("Bob","Hi"))

#Medium functions 
#first function
def calculate_total(*prices,discount=0):
    total = sum(prices)
    if discount:
        total *= (1 - (discount/100))
    return total
# Test cases
print(calculate_total(10, 20, 30,discount=0))
print(calculate_total(10, 20, 30, discount=10))

# Second function
def create_multiplier(num):
    def multiplier(x):
        return num * x
    return multiplier

# Test cases
doble = create_multiplier(2)
triple = create_multiplier(3)
print(doble(5))
print(triple(5))

# Hard functions
# First function
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
    
# Test cases
print(power(2, 10))
print(power(3,4))

# Second function
def compose(*functions):
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed
def add_one(x):
    return x + 1
def double(x):
    return x * 2
def square(x):
    return x ** 2

# Test cases
f = compose(square, double, add_one)
print(f(3))
    











