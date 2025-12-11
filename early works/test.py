# while 1:
#     answer = input("Ты гей? - Да/Нет: ")
#     if answer == "да":
#         da = input("А твои родители знают что ты гей? - Да/Нет: ")
#         if da == 'Да':
#              continue
#         else:
#             continue
#     elif answer == "нет":  
#         no = input("А твои родители знают что ты гей? - Да/Нет: ")
#         if no == 'Нет':
#              continue
#         else:
#             continue

people = ['Mary', 'Bobby', 'Dean', 'Mas', 'John', 'Kas', 33, 44,11,23.4, False]
names = []
ages = []

for i in people:
    if type(i) == str:
        names.append(i)
    else:
        ages.append(i)


ages.remove(False)
ages.sort()
names[3] = 'Sam'
names.reverse()
print(names)
print(ages)