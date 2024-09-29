
'''
Є список з чисел, написати функції, які виводять усі числа:
    1) Більші за 5
    2) Менші за 0
'''

number_list = [-5, -7, 5, 4, 3, 8, 12]

# def print_numbers_greater_than_five(number_list):
#     for number in number_list:
#         if number > 5:
#             print(number)

def print_numbers_greater_than_five():
    for number in number_list:
        if number > 5:
            print(number)

# print_numbers_greater_than_five()

def print_numbers_less_than_zero(lst):

    def print_numbers():
        for number in lst:
            if number < 0:
                print(number)

    print_numbers()
    # for number in number_list:
    #     if number < 0:
    #         print(number)


print_numbers_less_than_zero(number_list)