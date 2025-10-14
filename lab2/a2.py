int('123е')
#Ошибка: ValueError: invalid literal for int() with base 10: '123е'
int('91.4')
#Ошибка: ValueError: invalid literal for int() with base 10: '91.4'
int(524.345 ** 435345345311145345)
#Ошибка: OverflowError: int too large to convert to float
int('7.1 + 4')
#Ошибка: ValueError: invalid literal for int() with base 10: '7.1 + 4'
int('4' - 2)
#Ошибка: TypeError: unsupported operand type(s) for -: 'str' and 'int'
int('4 - 2')
#Ошибка: ValueError: invalid literal for int() with base 10: '4 - 2'
int('42')
#можно
int(-12.12)
#можно
