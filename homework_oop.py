class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Метод для оценки лектора студентом"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        """Метод для расчета средней оценки за домашние задания"""
        all_grades = sum([grades for grades_list in self.grades.values() for grades in grades_list])
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(all_grades / total_count, 1) if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\
                \nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}')

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """Метод для расчета средней оценки за лекции"""
        all_grades = sum([grades for grades_list in self.grades.values() for grades in grades_list])
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(all_grades / total_count, 1) if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Метод для оценки студента проверяющим"""
        if isinstance(student, Student) and course in student.finished_courses or course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


#задание_1
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print('---\nЗадание 1\n---')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

#задание_2
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print('---\nЗадание 2\n---')
print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(lecturer.grades)  # {'Python': [7]}

# #задание_3
some_student = Student('Ruoy', 'Eman', 'Мужской')
some_student.courses_in_progress.append('Python')
some_student.courses_in_progress.append('Git')
some_student.finished_courses.append('Введение в программирование')
some_student.grades['Python'] = [10, 9]
some_student.grades['Git'] = [10]

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades['Python'] = [10, 9.8]

some_reviewer = Reviewer('Some', 'Buddy')

print('---\nЗадание 3\n---')
print(some_student, '\n')
print(some_lecturer, '\n')
print(some_reviewer, '\n')

#задание_4
#создаем студентов
student_1 = Student('Анастасия', 'Соколова', 'female')
student_1.courses_in_progress.extend(['Python', 'Git'])
student_1.finished_courses.append('Введение в программирование')
student_2 = Student('Иван', 'Иванов', 'male')
student_2.courses_in_progress.append('Python')
student_2.finished_courses.extend(['Git', 'Введение в программирование'])

#создаем лекторов
lecturer_1 = Lecturer('Александр', 'Александров')
lecturer_1.courses_attached.append('Введение в программирование')
lecturer_2 = Lecturer('Михаил', 'Михайлов')
lecturer_2.courses_attached.extend(['Python', 'Git'])

#создаем проверяющих
reviewer_1 = Reviewer('Максим', 'Максимов')
reviewer_2 = Reviewer('Сергей', 'Сергеев')

#студенты ставят оценки лекторам
student_1.rate_lecture(lecturer_1, 'Введение в программирование', 10)
student_1.rate_lecture(lecturer_2, 'Python', 9)
student_1.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_1, 'Введение в программирование', 8)
student_2.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Git', 10)

#проверяющие ставят оценки за домашние задания

reviewer_1.rate_hw(student_1, 'Введение в программирование', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Введение в программирование', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Git', 8)

#показываем информацию о студентах, лекторах и проверяющих
print('---\nЗадание 4\n---')
print('Студенты:\n')
print(student_1, '\n')
print(student_2, '\n')
print('Лекторы:\n')
print(lecturer_1, '\n')
print(lecturer_2, '\n')
print('Проверяющие:\n')
print(reviewer_1, '\n')
print(reviewer_2, '\n')

print('---\nПроверяем работу методов расчета средней оценки и их сравнение\n---')
print(f'Средняя оценка студента {student_1.name} {student_1.surname} - {student_1.average_grade()}')
print(f'Средняя оценка студента {student_2.name} {student_2.surname} - {student_2.average_grade()}')
print(student_1.average_grade() > student_2.average_grade()) #true
print(student_1.average_grade() == student_2.average_grade()) #false
print(f'Средняя оценка лектора {lecturer_1.name} {lecturer_1.surname} - {lecturer_1.average_grade()}')
print(f'Средняя оценка лектора {lecturer_2.name} {lecturer_2.surname} - {lecturer_2.average_grade()}')
print(lecturer_1.average_grade() < lecturer_2.average_grade()) #false
print(lecturer_1.average_grade() != lecturer_2.average_grade()) #true

def average_homework_grade_calc(students, course):
    """Функция для расчета средней оценки за домашние задания по курсу"""
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])  # Добавляем оценки текущего студента
    if grades:
        return round(sum(grades) / len(grades), 1)
    else:
        return 0

def average_lecture_grade_calc(lecturers, course):
    """Функция для расчета средней оценки лектора по курсу"""
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])  # Добавляем оценки текущего лектора
    if grades:
        return round(sum(grades) / len(grades), 1)
    else:
        return 0

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

print('---\nПроверяем работу созданных функций:\n---')
print(f'Средняя оценка за домашние задания по курсу "Python" - {average_homework_grade_calc(students, 'Python')}')
print(f'Средняя оценка лектора на курсе "Python" - {average_lecture_grade_calc(lecturers, 'Python')}')