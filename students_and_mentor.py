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

    # считаем среднюю оценку по всем домашкам
    def _get_average_grade(self):
        """Вспомогательный метод для подсчёта средней оценки."""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    # переопределяем str
    def __str__(self):
        # форматируем курсы через запятую
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

    # сравнение студентов - по средней оценке
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

    # средняя оценка за лекции
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

    # сравнение лекторов - тоже по средней оценке
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

    # у проверяющего самый простой str
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# быстрая проверка магических методов
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Мария', 'Сидорова')
reviewer = Reviewer('Пётр', 'Петров')
student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Дмитрий', 'Борисов', 'М')

# проверяем __str__
print(reviewer)
print()
print(lecturer1)
print()
print(student1)

# проверяем сравнение
print()
print('Сравнение лекторов:', lecturer1 > lecturer2)
print('Сравнение студентов:', student1 < student2)