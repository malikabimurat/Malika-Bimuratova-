import os
import shutil

# 1. Список только директорий, только файлов и всех объектов в указанном пути
def list_contents(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All contents:", os.listdir(path))

list_contents(".")  # Укажите нужный путь

# 2. Проверка доступа к указанному пути (существование, чтение, запись, выполнение)
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

check_access("sample.txt")  # Укажите нужный путь

# 3. Проверка существования пути и нахождение имени файла и директории
def path_info(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

path_info("sample.txt")  # Укажите нужный путь

# 4. Подсчет количества строк в текстовом файле
def count_lines(file_path):
    with open(file_path, "r") as file:
        print("Number of lines:", sum(1 for _ in file))

count_lines("sample.txt")  # Укажите нужный путь

# 5. Запись списка в файл
def write_list_to_file(file_path, data):
    with open(file_path, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

write_list_to_file("output.txt", ["apple", "banana", "cherry"])

# 6. Генерация 26 текстовых файлов (A.txt, B.txt, ..., Z.txt)
def generate_files():
    for letter in range(65, 91):  # ASCII коды от 'A' до 'Z'
        with open(chr(letter) + ".txt", "w") as file:
            file.write(f"File {chr(letter)}.txt created.\n")

generate_files()

# 7. Копирование содержимого одного файла в другой
def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"Contents of {source} copied to {destination}")

copy_file("sample.txt", "copy_sample.txt")  # Укажите нужные файлы

# 8. Удаление файла после проверки существования и доступа
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):  # Проверка прав на запись
            os.remove(file_path)
            print(f"File {file_path} deleted.")
        else:
            print("No permission to delete the file.")
    else:
        print("File does not exist.")

delete_file("copy_sample.txt")
