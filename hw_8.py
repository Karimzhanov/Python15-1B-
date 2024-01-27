# Задача 1 
# import random

# def write_random_to_file(language_list):
#     random_language = random.choice(language_list)
    
#     file = open("result.txt", "w")
#     file.write(random_language)
#     file.close()

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]
# write_random_to_file(language)

# Задача 2
# text1 = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum"""

# text = open('text.txt', 'w')
# text.write(text1)
# text.close()


# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum"""

# with open('text1.txt', 'w') as file:
#     file.write(text)

# Доп Задача t
# file = open("text.txt", "r")
# text_content = file.read()
# file.close()

# new_file = open("wikipedia.txt", "w")
# new_file.write(text_content)
# new_file.close()