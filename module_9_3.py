# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для first_result
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для second_result
second_result = (len(first[i]) > len(second[i]) for i in range(min(len(first), len(second))))

# Примеры использования генераторов
print(list(first_result))  # Преобразуем в список для вывода
print(list(second_result))  # Преобразуем в список для вывода