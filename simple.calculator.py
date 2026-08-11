num1 = float(input('num1= '))
num2 = float(input('num2= '))
symbol = input('symbol= ')

if symbol == '+':
    sum = num1 + num2
    print(f'{num1} + {num2} = {sum}')
elif symbol == '-':
    difference = num1 - num2
    print(f'{num1} - {num2} = {difference}')
elif symbol == '*':
    product = num1 * num2
    print(f'{num1} * {num2} = {product}')
elif symbol == '/':
    divide = num1 / num2
    if num2 != 0
       print(f'{num1} / {num2} = {divide}')
    else:
        print('Invalid')
elif symbol == '^':
    power = num1 ** num2
    print(f'{num1} ** {num2} = {power}')
elif symbol == '%':
    mod = num1 * (num2/100)
    print(f'{num1} % {num2} = {mod}')
else:
    print('Error')
