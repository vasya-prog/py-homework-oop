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

    # новый метод - студент может оценить лекцию
    def rate_lecture(self, lecturer, course, grade):
        """Метод для выставления оценки лектору за лекцию."""
        # проверяем что оценим именно лектора, а не кого попало
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


class Lecturer(Mentor):
    """Класс лектора. Наследуется от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    """Класс проверяющего. Наследуется от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)

    # метод rate_hw теперь только у Reviewer
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


# проверяем как работает
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# студент оценивает лекции
print(student.rate_lecture(lecturer, 'Python', 7))  # None - ок
print(student.rate_lecture(lecturer, 'Java', 8))    # Ошибка - лектор не ведёт Java
print(student.rate_lecture(lecturer, 'C++', 8))     # Ошибка - студент не изучает C++
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка - это не лектор

print(lecturer.grades)  # {'Python': [7]}