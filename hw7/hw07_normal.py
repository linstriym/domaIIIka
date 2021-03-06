# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
#TODO:
class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
 
    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname
 
    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())
 
 
# if __name__ == '__main__':  # Тестирование.
#     people1 = People('Иван', 'Иванович', 'Иванов')
#     print(people1.get_full_name())
#     print(people1.get_short_name())
 
 
class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class
 
 
# if __name__ == '__main__':  # Тестирование.
#     st_1 = Student('Семен', 'Семенович', 'Семенов', 'Анна Михайлова', 'Алексанр Семенов', '7а')
#     st_2 = Student('Сергей', 'Сергеевич', 'Сергеев', 'Ольга Сергеева', 'Андрей Сергеев', '7б')
#     st_3 = Student('Олег', 'Олегович', 'Петров', 'Юлия Петрова', 'Олег Петров', '7а')
#     print(Student.all_classes(st_1))
 
 
class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
 
 
class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}
 
 
 
if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Иванов', 'Иван', 'Иванович', 'Математика'),
                Teacher('Петров', 'Петр', 'Петрович', 'Литература'),
                Teacher('Николаев', 'Артем', 'Сидорович', 'Физика'),
                Teacher('Дмитриев', 'Дмитрий', 'Дмитриевич', 'История'),
                Teacher('Никитов', 'Никита', 'Никитович', 'Биология')]
    classes = [Class_rooms('11 А', [teachers[3], teachers[1], teachers[0]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[0], teachers[1], teachers[2]])]
    parents = [People('Семенов', 'Семен', 'Семенович'),
               People('Орлова', 'Светлана', 'Семеновна'),
               People('Романов', 'Роман', 'Романович'),
               People('Ритинова', 'Рита', 'Антоновна'),
               People('Сергеев', 'Сергей', 'Сергеевич'),
               People('Степина', 'Анастасия', 'Николаевна')]
    students = [Student('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], classes[0]),
                Student('Ольга', 'Романова', 'Романова', parents[2], parents[3], classes[1]),
                Student('Александр', 'Сергеевич', 'Сергеев', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)
 
    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())
 
    # for f in students:
    #     print('Список предметов ученика {}'.format(f.school_class))
    #     for teacher in classes[0].teachersdict.values():
    #         print(teacher.get_full_name())
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
#TODO:
students = []
teachers = []


def get_clases():
    # 1. Получить полный список всех классов школы
    classes = set()
    for student in students:
        classes.add(student.class_room)
    return classes
def students_by_class(current_class):

    for student in students:
        if student.class_room == current_class:
            return student.get_fio()
def get_subjects(current_student):
    # 3. Получить список всех предметов указанного ученика
    current_teachers = []
    current_subjects = []
    for student in students:
        if (student.surname, " ", student.name, " ", student.patronymic) == current_student:
            current_class = student.class_room
    try:
        for teacher in teachers:
            if current_class in teacher.teach_classes:
                current_teachers.append(teacher)
    except UnboundLocalError:
        return ('Ученик не найден')

    for current_teacher in current_teachers:
        current_subjects.append(current_teacher.subject)
    return current_subjects
def get_parents(current_student):
    # 4. Узнать ФИО родителей указанного ученика
    for student in students:
        if (student.surname, " ", student.name, " ", student.patronymic) == current_student:
            return student.parents
def get_teachers_by_class(current_class):
    # 5. Получить список всех Учителей, преподающих в указанном классе
    current_teachers = []
    for teacher in teachers:
        if current_class in teacher.teach_classes:
            current_teachers.append(teacher)
    return current_teachers 