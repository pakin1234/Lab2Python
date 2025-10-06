'''5. Реализовать декоратор, который выводит в консоль время выполнения декорируемой функции. Протестировать работу декоратора на двух функциях:
	- Функция вычисляет сумму двух чисел a и b, выводит результат в консоль
	- Функция читает из файла input.txt значение двух чисел a и b, записывает результат вычисления в файл output.txt (файлы приложить к репозиторию)'''
import time

def time_control(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start
        print(f"Время выполнения: {end:.6f} секунд")
    return wrapper

@time_control
def sum_numbers(number1: float, number2: float):
    result = number1 + number2
    print(f"Сумма двух чисел: {result}")

@time_control
def sum_file():
    with open("input.txt") as f:
        nums = f.read().split()

    a, b = map(float, nums)
    result = a + b

    with open("output.txt", 'w') as f:
        f.write(str(result))

sum_numbers(12345345435.5435345435, 98794569476.54634568)
sum_file()


