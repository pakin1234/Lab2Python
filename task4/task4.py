'''4. Создать классы студент, аспирант. Студент содержит свойства: номер группы, средний балл. Аспирант отличается от студента наличием научной работы (название работы в виде строки). Реализовать в классах следующие методы: 
	- вывести информацию о человеке (фио, возраст)
	- вывести размер стипендии. Если средняя оценка равна 5, то стипендия 8000р для аспиранта и 6000р для студента, если меньше 5, то стипендия для аспиранта 6000р, для студента 4000р, в других случаях стипендия 0р
	- Сравнение размера стипендии с другим студентом/аспирантом (больше или меньше)'''
class Student:
    full_scholarship = 6000
    less_scholarship = 4000
	excellent_mark = 5
	good_mark = 4

    def __init__(self, surname: str, name: str, middle_name: str, age: int, group_number: str, gpa: float):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.age = age
        self.group_number = group_number
        self.gpa = gpa
    
    def info(self) -> str:
        return f"ФИО: {self.surname} {self.name} {self.middle_name}; Возраст: {self.age}"
    
    def scholarship(self) -> int:
        if self.gpa == excellent_mark: return self.full_scholarship
        elif good_mark <= self.gpa < excellent_mark: return self.less_scholarship
        else: return 0

    def compare_scholarship(self, other_student) -> str:
        if not isinstance(other_student, Student):
            raise ValueError("Сравниваемый объект должен быть студентом или аспирантом")
        scholarship1 = self.scholarship()
        scholarship2 = other_student.scholarship()
        if scholarship1 > scholarship2:
            return f"Стипендия {self.surname}а больше чем у {other_student.surname}а"
        elif scholarship1 < scholarship2:
            return f"Стипендия {self.surname}а меньше чем у {other_student.surname}а"
        else:
            return "Стипендии одинаковые"
        
class Aspirant(Student):
    full_scholarship = 8000
    less_scholarship = 6000

    def __init__(self, name: str, surname: str, middle_name: str, age: int, group_number: str, gpa: float, scientific_work: str):
        super().__init__(name, surname, middle_name, age, group_number, gpa)
        self.scientific_work = scientific_work

def main():
    student1 = Student("Иванов", "Иван", "Иванович", 20, "12345-542", 4.7)
    student2 = Aspirant("Смирнов", "Дмитрий", "Дмитриевич", 24, "98766-123", 5, "Разработка алгоритма оптимизации маршрутов")
    print(student1.info())
    print(student1.scholarship())
    print(student2.info())
    print(student2.scholarship())
    print(student1.compare_scholarship(student2))

if __name__ == "__main__":
	main()
