import os

# Створюємо директорії
os.makedirs("Dir_1/Dir_2", exist_ok=True)
os.makedirs("Dir_1/Dir_3", exist_ok=True)

# Список файлів + у які папки їх класти
files = {
    "Dir_1": ["file_1"],
    "Dir_1/Dir_2": ["file_2", "file_3"],
    "Dir_1/Dir_3": ["file_4"],
}

# Створення файлів
for folder, file_list in files.items():
    for filename in file_list:
        with open(f"{folder}/{filename}.txt", "w") as f:
            f.write(f"This is {filename}")  # будь-який текст
