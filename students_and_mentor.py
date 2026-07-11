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

    def rate_lecture(self, lecturer, course, grade):
        """Метод для выставления оценки лектору за лекцию."""
        if isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_average_grade(self):
        """Вспомогательный метод для подсчёта средней оценки."""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        avg = self._get_average_grade()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {avg}\n'
            f'Курсы в процессе изучения: {in_progress}\n'
            f'Завершенные курсы: {finished}'
        )

    def __lt__(self, other):
        return self._get_average_grade() < other._get_average_grade()

    def __gt__(self, other):
        return self._get_average_grade() > other._get_average_grade()

    def __eq__(self, other):
        return self._get_average_grade() == other._get_average_grade()


class Mentor:
    """Базовый класс для преподавателей."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лектора. Наследуется от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        """Вспомогательный метод для подсчёта средней оценки за лекции."""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg = self._get_average_grade()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {avg}'
        )

    def __lt__(self, other):
        return self._get_average_grade() < other._get_average_grade()

    def __gt__(self, other):
        return self._get_average_grade() > other._get_average_grade()

    def __eq__(self, other):
        return self._get_average_grade() == other._get_average_grade()


class Reviewer(Mentor):
    """Класс проверяющего. Наследуется от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Метод для выставления оценки студенту за домашнее задание."""
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# ===================== функции для подсчёта средних =====================

def get_average_students_grade(students, course):
    """Считает среднюю оценку всех студентов из списка по конкретному курсу."""
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)


def get_average_lecturers_grade(lecturers, course):
    """Считает среднюю оценку всех лекторов из списка по конкретному курсу."""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)


# ===================== полевые испытания =====================

# создаём по 2 экземпляра каждого класса
student1 = Student('Ольга', 'Алёхина', 'Ж')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Дмитрий', 'Борисов', 'М')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Основы HTML']

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Мария', 'Сидорова')
lecturer2.courses_attached += ['Python', 'Java']

reviewer1 = Reviewer('Пётр', 'Петров')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Анна', 'Смирнова')
reviewer2.courses_attached += ['Python', 'Java']

# проверяющие оценивают студентов
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Java', 6)

# студенты оценивают лекторов
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Git', 8)
student1.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Java', 8)

# проверяем __str__ для всех
print('=== Проверяющий ===')
print(reviewer1)
print()
print('=== Лектор ===')
print(lecturer1)
print()
print('=== Студент ===')
print(student1)
print()

# проверяем сравнение
print('Сравнение лекторов (lecturer1 > lecturer2):', lecturer1 > lecturer2)
print('Сравнение студентов (student1 > student2):', student1 > student2)
print()

# проверяем функции подсчёта
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

avg_hw_python = get_average_students_grade(students_list, 'Python')
avg_lecture_python = get_average_lecturers_grade(lecturers_list, 'Python')

print(f'Средняя оценка студентов за ДЗ по курсу Python: {avg_hw_python}')
print(f'Средняя оценка лекторов за лекции по курсу Python: {avg_lecture_python}')