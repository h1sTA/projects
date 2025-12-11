# def average_arif(a,b):
#     plus = a + b
#     avg = plus / 2
#     print(avg)
# average_arif (10,5)


# def shout(name):
#     return name.upper()

# # shname = shout("isac")
# # print(shname)

# print(shout('isac'))


# def example():
#     print('готово')
    
# example()

# def example():
#     return 'готово'
#     print('этот код никогда не выполнится')


# def truncate(text, length):
#     # BEGIN (write your solution here)
#     stratched = (text[:length] + '...')
#     return stratched

# print(truncate('Fortnite', 3))
#     # END

# def truncate(text, lenght):
#     stratched = f'{text[0:lenght]}...'
               
#     return stratched
# print (truncate("Battlefield", 4))

# print ("hum" * 3)

# def repeat(text, times):
#     return text * times
# print(repeat("Hi", 3))


# print (int(input("Cколько тебе лет?")))

# def get_hidden_card(credit = 16, cens, stars = '*'):
#     cenzuring = credit[:cens]
#     return stars + cenzuring
# print (get_hidden_card(132674789278832784, -4))

# def get_hidden_card(card_number, stars_count=4):
#     visible_digits_line = card_number[-4:]
#     return f"{'*' * stars_count}{visible_digits_line}"
# get_hidden_card('1234567812345678', 6)

# def describe(name: str, age: int, height: float) -> str:
#     return f"{name}, {age} лет, рост {height}"
# print(describe("Anna", 25, 1.70))

# x = 2
# y = 3
# # print(f"x + y = x + y")       # ❌ неправильно
# print(f"x + y = {x + y}")     # ✅ правильно

# for i in range(3):
#     print(i)

# def word_multiply(text: str, n: int = 0) -> str:
#     return f'{text * n}'
# print (word_multiply("python", 3))

# def is_infant(age: int) -> bool:
#     return age < 2
# print(is_infant(1))

# def is_pensioner(number: int,) -> bool:
#     return number >=60
# print(is_pensioner(61))


# def is_international_phone(num: str) -> bool:
#     first_letter = num[0]
#     return first_letter == "+"
# print (is_international_phone("+89602223423"))

# def is_international_phone(num:str) -> bool:
#     return num[0] == "+"
# print(is_international_phone("89602223423"))

# def is_even(number: int) -> bool:
#     return number % 2 == 0

# print(is_even(10))  # => True
# print(is_even(3))   # => False

# def is_leap_year(year:int) -> bool: #выскокосный год
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(is_leap_year(2028))

# print('Фортнайт'[0::7])

# def is_palindrome(word: str) -> bool:
#     lower_word = word.lower()
#     return lower_word == lower_word[::-1]


# def is_not_palindrome(word: str) -> bool:
#     return not is_palindrome(word)

# number = 20-30
# result = number > 0 and "positive" or "non-positive"
# print(result)

# if 2 > 3:
#     print("Yes, it is true")

# def guess_number(num: int,) -> str:
#     if num == 42:
#         return ('You win!')
#     return ('Try again!')
# print (guess_number(42))

# Решение учителя:
# def normalize_url(url: str) -> str:
#     prefix = "https://"
#     if url[:8] == prefix:
#         return url
#     else:
#         if url[:7] == "http://":
#             return prefix + url[7:]
#         else:
#             return prefix + url
# Ваше решение:
# def normalize_url(adres: str) -> str:
#     if adres.startswith("https://"):
#         return adres
#     elif adres.startswith("http://"):
#         return "https://" + adres[7:]  # убираем "http://", добавляем https://
#     else:
#         return "https://" + adres

# print(normalize_url('google.com'))       # https://google.com
# print(normalize_url('http://example.com')) # https://example.com
# print(normalize_url('https://hexlet.io'))  # https://hexlet.io


# adres = "//hhtps:"
# site = "//htorrent_igruha"
# correct = adres + site[3:17]
# print(correct)

# def who_is_this_house_to_starks(family: str) ->str:
#     if family == 'Karstark' or family == 'Tully':
#         return 'friend'
#     elif family == 'Lannister' or family == 'Frey':
#         return 'enemy'
#     else:
#         return 'neutral'

# print(who_is_this_house_to_starks('Karstark'))
# print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
# print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
# print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'

# def flip_flop(text: str) -> str:
#     if text == 'flip':
#         return "flop"
#     else:
#         return 'flip'

# print(flip_flop('flip'))
# print(flip_flop('flop'))
# print(20*'.')

# def flip_flop_2(text):
#     return 'flop' if text =='flip' else 'flop'

# print(flip_flop('flip'))
# print(flip_flop('flop'))

# def get_number_explanation(num):
#     match num:
#         case 666:
#             return "devil number"
#         case 42:
#             return "answer for everything"
#         case 7:
#             return "prime number"
#         case _:
#             return "just a number"
    
# get_number_explanation(8)  # just a number
# get_number_explanation(666)  # devil number
# get_number_explanation(42)  # answer for everything
# get_number_explanation(7)  # prime number
               
               
def print_numbers(n: int) -> None:
    i = 1
    while i <= n:
        print(i)
        i = i + 1
    print("Finished!")


def multiply_numbers_from_range(start: int, finish: int) -> int:
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result


def multiply_numbers_from_range(start, finish):
    i = start
    sum = 1
    while i <= finish:
        sum = sum * i
        i = i + 1
    return sum

multiply_numbers_from_range(2, 5)


def sum_numbers_from_range(start: int, finish: int) -> int:
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    sum = 0  # Инициализация суммы
    while i <= finish:  # Двигаемся до конца диапазона
        sum = sum + i   # Считаем сумму для каждого числа
        i = i + 1       # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    return sum

def add_spaces(text):
    result = ''
    i = 0
    while i < len(text):
        result = result + text[i]
        if i != len(text) - 1:   # если это не последняя буква — добавляем пробел
            result = result + ' '
        i = i + 1
    return result
