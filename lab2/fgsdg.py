try:
    print(int('123е'))
except Exception as e:
    print(f"1. Ошибка: {type(e).__name__}: {e}")
try:
    print(int('91.4'))
except Exception as e:
    print(f"2. Ошибка: {type(e).__name__}: {e}")
try:
    print(int('7.1 + 4'))
except Exception as e:
    print(f"4. Ошибка: {type(e).__name__}: {e}")
try:
    print(int('4' - 2))
except Exception as e:
    print(f"5. Ошибка: {type(e).__name__}: {e}")
try:
    print(int('4 - 2'))
except Exception as e:
    print(f"6. Ошибка: {type(e).__name__}: {e}")
try:
    print(f"7. Результат: {int('42')}")
except Exception as e:
    print(f"7. Ошибка: {type(e).__name__}: {e}")
try:
    print(f"8. Результат: {int(-12.12)}")
except Exception as e:
    print(f"8. Ошибка: {type(e).__name__}: {e}")