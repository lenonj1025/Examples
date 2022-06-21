# Method 2
import my_math_utility

print(my_math_utility.addition(10, 20))
print(my_math_utility.subtraction(10, 20))
print(my_math_utility.pi)


# Method 2
import my_math_utility as mmu

print(mmu.addition(10, 20))
print(mmu.subtraction(10, 20))
print(mmu.pi)

# Method 3
from my_math_utility import addition, subtraction, pi
print(addition(10, 20))
print(subtraction(10, 20))
print(pi)
