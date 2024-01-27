# Задача 1
# Исключения это ситуации или исключения(exceptions) - это ошибки, обнаруженные при исполнении. Например, к чему приведет попытка чтения несуществующего файла? Или если файл был случайно удален пока программа работала? Такие ситуации обрабатываются при помощи исключений
#  Задача 2
#  try: 
#      name = "kyky"
#      print(name1)
#  except NameError:
#      print("обработали ошибку")

#  try:
#      num = [1, 2, 3, 4]
#      print(num[2])
# except IndexError:
#     print("такого индекса нет")

# Задача 3
# num1 = input("Введите числа разделнные запятной: ")
# print(set(num1))

# # Доп Задача 
# while True:
#     try:
#         num1 = int(input("Первое число: "))
#         num2 = int(input("Второе число: "))
#         operator = input("+, -, *, /:")
#         if operator == "+":
#             result = num1+num2
#             print(result)
#             if result % 2 == 0:
#                 print('Сумма четная')
#             else:
#                 print("Сумма нечетная")
#         elif operator == "-": 
#             result1 = num1-num2
#             print(result1)
#             if result1 % 2 == 0:
#                 print('Сумма четная')
#             else:
#                 print("Сумма нечетная")
#         elif operator == "*":
#             result2 = num1*num2
#             print(result2)
#             if result2 % 2 == 0:
#                 print('Сумма четная')
#             else:
#                 print("Сумма нечетная")
#         elif operator == "/":
#             try:
#                 result3 = num1/num2
#                 print(result3)
#                 if result3 % 2 == 0:
#                     print('Сумма четная')
#                 else:
#                     print("Сумма нечетная")
#             except ZeroDivisionError:
#                 print("деление на ноль невазможно")
        
#     except ValueError:
#      print("Введите число!")

# Задача 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

# Задача 2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' :3, 'num_100' : 100}
# print(numbers['num_1'] *5, numbers['num_2']*5, numbers['num_3']*5,numbers ['num_100'] *5)

# Задача 3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age']*= 2
# print(student)

# Задача 4
# student = {'nam' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16 
# print(student)

# Задача 5
# student = {'name' : 'Askhat', 'age' : 17}
# del student['age']
# print(student)

# Задача 6
# student = {'name' : 'Askhat'}
# student['address'] = "Западный Анар)"
# print(student)

# Доп Задача 2
# while True:
    # chat_bot = input("Введите текст : ")
    # if "?" in chat_bot:
    #     print("Конечно!")
    # elif "!" in chat_bot: 
    #     print("Успокойся")      
    # elif chat_bot == "":
    #     print("Как классно, когда ты молчишь")
    # else : 
    #     print("Ну и что")

 
# text = input("Введите текст для сокращение: ") 
# razdel = text.split() 
# a = [] 
# for word in razdel: 
#     a.append(word[0].upper()) 
# b = "".join(a) 
# print(b) 
     
# a ="""Money, Money, Money, it's always sunny, in the richmens world"""
# print(a.count('Money'))
# print(a.count("it's"))
# print(a.count('always'))
# print(a.count('sunny'))
# print(a.count('in'))
# print(a.count('the'))
# print(a.count("richmens"))
# print(a.count('world'))

# def isogram(word):
#     word = word.lower()
#     letters = set()
#     for letter in word:
#         if letter in letters:
#             return False
#         letters.add(letter)
#     return True
# word1 = "Hello"
# print(isogram(word1))

# def nab(n):
#     print(int(str(n)[::-1]))
# nab(27)
