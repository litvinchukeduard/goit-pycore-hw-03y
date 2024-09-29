'''
Написати функцію, яка буде памʼятати скільки разів її викликали
'''

counter = 0
lst = []

def count_times():
    global counter
    # lst.append(1)
    # lst = [1, 2, 3]
    counter = counter + 1
    print(f'Times called: {counter}')


def count_times_nonlocal():
    counter = 0
    def print_count():
        nonlocal counter
        counter = counter + 1
        print(f'Times called: {counter}')
    return print_count


count_times()
count_times()
count_times()
count_times()
print(lst)

count_times_nonlocal()()