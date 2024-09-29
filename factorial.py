'''
Написати функцію, яка буде рекурсивно рахувати факторіал
'''

# factorial(6) = 6 * 5 * 4 * 3 * 2 * 1
# factorial(1) = 1

# factorial(6) = 6 * factorial(5)
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)

# factorial(2) = 2 * 1 = 2
# factorial(3) = 3 * 2
# def factorial(number):
#     if number == 1:
#         return 1
#     return number * factorial(number - 1) # Ctrl / (Command /)

def factorial(number, level=0):
    if number == 1:
        print(f'Level {level}: factorial(1) = 1')
        return 1
    
    print(f'Level {level}: factorial({number}) = {number} * factorial({number} - 1)')
    result = number * factorial(number - 1, level=level + 1)
    print(f'Level {level}: factorial({number}) = {result}')
    return result


print(factorial(1))
print()
print(factorial(6))