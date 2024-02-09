# Write a function say_hi that introduces a person based on the provided parameters.
#
# Input: Two arguments, a string (str) and a positive integer (int).
#
# The function should return a string.
#
# Replace pass with your solution.
# def say_hi(name, age):
#     pass
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

def say_hi(name, age):
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
