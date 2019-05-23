import re

nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'for', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve', 13: 'thirteen', 14: 'forteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
decades = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
large_nums = {0: 'thousand', 1: 'million', 2: 'billion', 3: 'trillion'}
operators = {'+': 'plus', '-': 'minus', '*': 'multiply', '/': 'divide'}


def convert_num(num):
    result = get_last_3(num % 1000)
    for i in range(0, len(large_nums)):
        if num < 1000:
            break
        result = get_last_3(divide(num, 1000) % 1000) + ' ' + large_nums[i] + ('' if divide(num, 1000) % 1000 == 1 else '\'s') +  ' ' + result
        num = divide(num, 1000)
    return str(result)


def get_last_3(num):
    result = get_last_2(num % 100)
    hundreds = divide(num, 100)
    if hundreds > 0:
        result = nums[hundreds] + ' hundred' + ('' if hundreds == 1 else '\'s') + ' ' + result
    return result


def get_last_2(num):
    if num < 20:
        return nums[num]
    last_sym = num % 10
    if last_sym != 0:
        last_sym = ' ' + nums[last_sym]
    else:
        last_sym = ''
    decade = divide(num, 10)
    return decades[decade] + last_sym


def divide(num, divider):
    return (num - num % divider) / divider


def convert_equality(equality):
    condition_re = r'[\d]+\s[\+\-\*\/]\s[\d]+\s=\s[\d]+'
    if re.match(condition_re, equality):
        splited_condition = equality.split(' ')
        num1 = splited_condition[0]
        num2 = splited_condition[2]
        num3 = splited_condition[4]
        operator = splited_condition[1]
        return convert_num(int(num1)) + ' ' + operators[operator] + ' ' + convert_num(int(num2)) + ' equals ' + convert_num(int(num3))
    else:
        return 'wrong input'


condition = input()
print(condition)
print(convert_equality(condition))
