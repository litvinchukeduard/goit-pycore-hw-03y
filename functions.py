
'''
Написати код, який буде рахувати зарплату
'''

lst_1 = [1000, 2000, 3000]
lst_2 = [100, 300, 100]
lst_3 = [111, 222, 100]

def count_salary(salary_list):
    sum = 0
    for number in salary_list:
        sum = sum + number

    tax = sum * 0.05
    return (sum - tax)

print(count_salary(lst_1))
print(count_salary(lst_2))
print(count_salary(lst_3))