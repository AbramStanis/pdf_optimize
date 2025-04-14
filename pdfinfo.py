import fitz
import sys
import pikepdf as pike

def get_metadata_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        print(doc.metadata)
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def select_and_save_pdf(file_input, file_output, a):
    try:
        doc = fitz.open(file_input)
        doc.select(a)
        doc.save(file_output)
        doc.close()
        return True
    except Exception as e:
        print(f"Ошибка при открытии PDF: {e}")
        return False

def compress_pdf(input_path, output_path):
    with pike.open(input_path) as pdf:
        pdf.save(output_path)


while True:
    num = int(input("\nВведите 1 для оптимизации файла pdf\n"
    "Введите 2 для извлечения страницы/страниц файла pdf\n" \
    "Введите 3 для просмотра метаданных файла pdf\n"))
    if num == 1:
        try:
            file_input = input("Поместите файл рядом с приложением и укажите его название с расширением: ")
            file_output = input("Укажите его наименование после оптимизации: ")
            compress_pdf(file_input, file_output)
        except Exception as e:
            print(f"Ошибка: {e}")
    elif num == 2:
        try:
            file_input = input("Поместите файл рядом с приложением и укажите его название с расширением: ")
            file_output = input("Укажите его наименование после извлечения: ")
            a = input("Укажите страницы для извлечения через запятую: ")
            a = a.split(",")
            int_values = [(int(value)-1) for value in a]
            select_and_save_pdf(file_input, file_output, int_values)
        except Exception as e:
            print(f"Ошибка: {e}")
    elif num == 3:
        try:
            file_input = input("Поместите файл рядом с приложением и укажите его название с расширением: ")
            get_metadata_pdf(file_input)
        except Exception as e:
            print(f"Ошибка: {e}")


