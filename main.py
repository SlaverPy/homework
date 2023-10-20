import collections


def calculate_character_frequency(file_path):
    # Используем collections.Counter для подсчета символов
    character_count = collections.Counter()

    # Определите размер буфера (в байтах), чтобы читать файл по частям
    buffer_size = 1024 * 1024  # 1 МБ, можно изменить по желанию

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break

            # Преобразуем байты в строки и учитываем только буквы и цифры
            data = data.decode('utf-8', errors='ignore')
            data = ''.join(filter(str.isalnum, data))

            # Обновляем счетчик символов
            character_count.update(data)

    total_characters = sum(character_count.values())

    # Выводим результат
    for char, count in character_count.items():
        frequency = (count / total_characters) * 100
        print(f'{char} — {frequency:.2f}%')


if __name__ == "__main__":
    file_path = 'путь_к_вашему_файлу.txt'  # Замените на путь к вашему файлу
    calculate_character_frequency(file_path)
