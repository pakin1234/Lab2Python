'''2. Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк. Сделать вызов данной функции для следующих функций фильтрации: 
	- Исключить строки с пробелами
	- Исключить строки, начинающиеся с буквы “a”
	- Исключить строки, длина которых меньше 5'''
from typing import Callable, List

def filter_strings(func: Callable, items: List[str]) -> List[str]:
    return [item for item in items if func(item)]


def main():
    phrase = ["hello", "jo ho", "asdf", "sdfsdf sg", "asdfasf"]

    print("Без пробелов:", filter_strings(lambda x : " " not in x, phrase))
    print("Не начинаются на 'a':", filter_strings(lambda x : not x.startswith("a"), phrase))
    print("Длина больше 5:", filter_strings(lambda x : len(x) > 5, phrase))

if __name__ == "__main__":
    main()
