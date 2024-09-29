
'''
Написати код, який по дсвіду рахує позицію розпобника
'''

# Junior: 0-1
# Middle: 2-4
# Senior: 4+

experience = 2
if 0 <= experience <= 1:
    print("Junior")
elif 2 <= experience <= 4:
    print('Middle')
elif experience > 4:
    print('Senior')

'''
Написати код, який приймає номер місяця і повертає значення місяця
'''
month = 1
if month == 1:
    print('January')
elif month == 2:
    print('February')

match month:
    case 1:
        print('January')
    case 2:
        print('February')