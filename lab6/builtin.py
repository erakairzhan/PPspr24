from math import prod
'''1
numbers = [1, 2, 3, 4, 5]
product = prod(numbers)
print(product)
'''

'''2
uppercase_count = 0
lowercase_count = 0
text = input()
for char in text:
  if char.isalpha(): 
    uppercase_count += char.isupper()
    lowercase_count += char.islower()
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
'''

'''3
text = input()
txet = text[::-1]
if text == txet :
    print("polidrome")
else:
    print("not")
'''

'''4
import time
import math
number = int(input())
delay_ms = int(input())
time.sleep(delay_ms / 1000)
result = math.sqrt(number)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
'''

'''5'''
my_tuple = (True, True, True)
all_true = all(my_tuple)
print(all_true) 