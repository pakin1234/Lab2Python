'''3. Создать иерархию классов Фигур: квадрат, прямоугольник, треугольник, круг. Каждый класс должен реализовывать следующие методы:
	- вычисление площади
	- вычисление периметра
	- сравнение площади с другой фигурой (больше или меньше)
	- сравнение периметра с другой фигурой (больше или меньше)'''
import math
from abc import ABC, abstractmethod

class Figure(ABC):
	@abstractmethod
	def area(self): pass
	
	@abstractmethod
	def perimeter(self): pass
	
	@abstractmethod
	def name(self): pass

	def compare_area(self, other_figure) -> str:
		if not isinstance(other_figure, Figure):
			raise ValueError("Сравниваемый объект должен быть фигурой")
		area1 = self.area()
		area2 = other_figure.area()
		if area1 > area2:
			return f"Площадь {self.name()}а больше {other_figure.name()}а"
		elif area1 < area2:
			return f"Площадь {self.name()}а меньше {other_figure.name()}а"
		else:
			return "Площади фигур равны"

	def compare_perimeter(self, other_figure) -> str:
		if not isinstance(other_figure, Figure):
			raise ValueError("Сравниваемый объект должен быть фигурой")
		perimeter1 = self.perimeter()
		perimeter2 = other_figure.perimeter()
		if perimeter1 > perimeter2:
			return f"Периметр {self.name()}а больше {other_figure.name()}а"
		elif perimeter1 < perimeter2:
			return f"Периметр {self.name()}а меньше {other_figure.name()}а"
		else:
			return "Периметры фигур равны"

class Square(Figure):
	def __init__(self, side: int | float):
		self.side = side

	def name(self) -> str:
		return "квадрат"
		
	def area(self) -> float:
		return self.side ** 2
	
	def perimeter(self) -> float:
		return 4 * self.side

class Rectangle(Figure):
	def __init__(self, length: int | float, width: int | float):
		self.length = length
		self.width = width

	def name(self) -> str:
		return "прямоугольник"
		
	def area(self) -> float:
		return self.length * self.width
	
	def perimeter(self) -> float:
		return 2 * (self.length + self.width)
		
class Triangle(Figure):
	def __init__(self, a: int | float, b: int | float, c: int | float):
		self.a = a
		self.b = b
		self.c = c

	def name(self) -> str:
		return "треугольник"
		
	def area(self) -> float:
		p = (self.a + self.b + self.c) / 2
		return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
	
	def perimeter(self) -> float:
		return self.a + self.b + self.c
		
class Circle(Figure):
	def __init__(self, radius: int | float):
		self.radius = radius

	def name(self) -> str:
		return "круг"
	
	def area(self) -> float:
		return math.pi * (self.radius ** 2)
	
	def perimeter(self) -> float:
		return 2 * math.pi * self.radius
	

def main():
	square = Square(25)
	circle = Circle(6.2)
	print(square.area())
	print(square.perimeter())
	print(circle.area())
	print(circle.perimeter())
	print(square.compare_area(circle))

if __name__ == "__main__":
	main()
	