# Home task 4. 05.06.2023
# 1. Пользователь вводит с клавиатуры строку.
# Посчитайте количество букв, цифр в строке. Выведите оба количества на экран. (использовать цикл)
string = input("Enter the string: ")
letter_count = 0
digit_count = 0

for char in string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("Quantity of letters:", letter_count)
print("Quantity of digits:", digit_count)
#
# 2. Пользователь вводит с клавиатуры строку и символ для поиска.
# Посчитайте сколько раз в строке встречается искомый символ. Полученное число выведите на экран.
string = input("Enter a string: ")
symbol = input("Enter a symbol for a search: ")

count = 0

for char in string:
    if char == symbol:
        count += 1

print("Quantity of symbols:", count)
#
# 3. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены.
# Произведите в строке замену одного слова на другое. Полученную строку отобразите на экране.
string = input("Enter a string: ")
word_to_find = input("Enter a word for a search: ")
word_to_replace = input("Enter a word for replace: ")

new_string = string.replace(word_to_find, word_to_replace)

print("Initial string:", string)
print("Final string:", new_string)
#
# 4. Дана строка. (сделать срезы)
# - Сначала выведите третий символ этой строки.
# - Во второй строке выведите предпоследний символ этой строки.
# - В третьей строке выведите первые пять символов этой строки.
# - В четвертой строке выведите всю строку, кроме последних двух символов.
# - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# - В седьмой строке выведите все символы в обратном порядке.
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# - В девятой строке выведите длину данной строки.
#
string = input("Enter a string: ")
# Третий символ
print("Third symbol:", string[2])
# Предпоследний символ
print("Penaltimate symbol:", string[-2])
# Первые пять символов
print("First 5 symbols:", string[:5])
# Строка без последних двух символов
print("String without last two symbols:", string[:-2])
# Символы с четными индексами
print("Symbols with even indexes:", string[::2])
# Символы с нечетными индексами
print("Symbols with odd indexes:", string[1::2])
# Символы в обратном порядке
print("Symbols in reverse order:", string[::-1])
# Символы через один в обратном порядке, начиная с последнего
print("Symbols one by one in reverse order:", string[::-2])
# Длина строки
print("Length of a string:", len(string))
# End of task