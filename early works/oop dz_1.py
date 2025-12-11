# #ООП - Объектно оринтированное программирование
# #Наследование от матери к ребенку - > 
# class Person:
#     #Создание атрибутов
#     def __init__(self, name, age, hair, height, education):
#         self.n = name
#         self.a = age
#         self.h = hair
#         self.he = height
#         self.e = education
    
#     def programming(self, language):
#         return f'{self.n} может программировать на {language}'

    
#     #Метод для вывода атрибутов в консоли
#     def __str__(self):
#         return f'Имя-{self.n}\nВозраст-{self.a}\nВолосы-{self.h}\nРост-{self.he}\nОбразование-{self.e}'
    
# person_1 = Person(name='Ivan', age=18, hair='brown', height=1.90, education=False)
# person_2 = Person(name='Ymyt', age=18, hair='white', height=2.0, education=False)

# print(person_1)
# print(person_1.programming('Java'))
# print('-'*20)
# print(person_2)
# print(person_2.programming('PHP'))
# print('-'*20)

# class Teacher(Person):
#     def __init__(self, name, age, hair, height, education, skills, iq):
#         super().__init__(name, age, hair, height, education)
#         self.sk = skills
#         self.iq = iq

#     def __str__(self):
#         return super().__str__()+f'\nОпыт-{self.sk}\nIQ-{self.iq}'
    

# person_3 = Teacher(name='Sam', age=21, hair='yellow', height=1.89, education=True, skills='MiddleDev', iq=150)
# print('-'*20)
# print(person_3)
# print(person_3.programming('JavaScript'))


# class Student(Teacher):
#     def __init__(self, name, age, hair, height, education, skills, iq, studing):
#         super().__init__(name, age, hair, height, education, skills, iq)
#         self.st = studing
    
#     def __str__(self):
#         return super().__str__()+f'\nОбучается-{self.st}'
    
# print('-'*20)    
# person_4 = Student("Sam", 21, "yellow", 1.89, True, "MiddleDev", 150, "1год")
# print(person_4)
#     # точно так же
    
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand   # свойство
#         self.color = color   # свойство

#     def drive(self):         # метод
#         print(f"{self.brand} едет!")

# # создаём объект
# my_car = Car("BMW", "чёрная")

# print(my_car.brand)  # BMW
# my_car.drive()       # BMW едет!














class Animal:
    def __init__(self, species, age, eats):
        self.s = species
        self.a = age
        self.e = eats
        
    def make_sound(self):
        print(f"{self.s} издает какой-то звук!")
    
    def __str__(self):
        return f'Животное: {self.s}\nВ среднем живет: {self.a}\nПитается: {self.e}'
    
animal_1 = Animal("Волк", "14-16 лет", "мясом")
print(animal_1)
animal_1.make_sound()
print(25*".")
class Mammal(Animal):
    def __init__(self, species, age, eats, fur_color):
        super().__init__(species, age, eats)
        self.f = fur_color
        
    def feed_milk(self):
        print(f'{self.s} кормит детенышей молоком')
        
    def __str__(self):
        return super().__str__()+f'\nИмеет цвет шерсти: {self.f}'
animal_2 = Mammal("Кошка", "13-20 лет", "мясом/кормом", "серый")
print(animal_2)
animal_2.feed_milk()
print(25*".")

class Reptile(Animal):
    def __init__(self, species, age, eats, poison):
        super().__init__(species, age, eats)
        self.po = poison
        
    def make_sound(self):
        return (f"{self.s} Шипит: Шшшш!")
        
    def crawwl(self):
        return ("Жиаотное ползает по земле")
    
    def __str__(self):
        return super(). __str__()+f"\nЭта особь: {self.po}"

animal_3 = Reptile("Гадюка", "14 лет", "мясом", "ядовитая")
print(animal_3)
print(animal_3.make_sound())
print(animal_3.crawwl())
print(25*".")

class Zoo_show:
    def __init__(self):
        self.shows = {
            1: {"name": "Шоу млекопитающих", "price": 500, "description": "Медведи танцуют, дельфины прыгают через кольца!"},
            2: {"name": "Шоу рептилий", "price": 300, "description": "Змеи шипят и ползают по арене!"},
            3: {"name": "Птичье шоу", "price": 400, "description": "Попугаи говорят и орлы летают над зрителями!"}
        }

    def show_info(self):
        print("🎪 Добро пожаловать в Зоопарк!\nСегодня у нас есть такие шоу:\n")
        for number, info in self.shows.items():
            print(f"{number}. {info['name']} — {info['description']}")
        print()

    def choose_show(self):
        choice = int(input("Введите номер шоу, которое хотите посетить: "))
        if choice in self.shows:
            info = self.shows[choice]
            print(f"\nВы выбрали: {info['name']}")
            print(f"💵 Цена билета: {info['price']} сом")
            print(f"🎬 Как проходит шоу: {info['description']}")
        else:
            print("Такого шоу нет! 😅")

zoo = Zoo_show()
zoo.show_info() 
zoo.choose_show()



