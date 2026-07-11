# Домашнее задание по теме "ООП: наследование, инкапсуляция, полиморфизм"
class Student:
    """Класс для описания студента."""

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        """Метод для выставления оценки лектору за домашнее задание."""
        if isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    """Базовый класс для преподавателей."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# теперь Mentor - родительский класс, от него наследуем
class Lecturer(Mentor):
    """Класс лектора. Наследуется от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        # у лектора будут хранить оценки за его лекции
        self.grades = {}


class Reviewer(Mentor):
    """Класс проверяющего. Наследуется от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)


# проверка что наследование работает
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True
print(lecturer.courses_attached)     # []
print(reviewer.courses_attached)     # []