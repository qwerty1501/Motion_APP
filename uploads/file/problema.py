# Задание №1 Множество наследование (ромбовидный)

class Super():                                                          # Класс 
    name = 'Sinon '                                                      # Имя
    age = 18                                                            # Возраст
    profession = ' Программист '                                          # Проффесия
    job = 'Motion Web '                                                  # Работа
    
    def __str__(self):
        return f'{self.name}'f'{self.age}'f'{self.profession}'f'{self.job}'
    

class Problem():
    job_list = 'Выполнил домашнее задание. '
    list_1 = 'Выполнено 4 задание из 6'
    
    def __str__(self):
        return f'{self.job_list}'f'{self.list_1}'
    

class Dastan(Super):
    name = 'Dastan '
    age = '19 лет '
    print('Hello')
    

a = Dastan()
print(a)


class Adi(Problem):
    print('Adi')
    
b = Adi()
print(b)