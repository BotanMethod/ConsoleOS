import os
import cmd
import time
import subprocess
from alive_progress import alive_bar

items = list(range(11))

with alive_bar(11) as bar:
    for item in items:
        print(f'Loading commands... / {item} from 11')
        time.sleep(1)
        bar()
time.sleep(5)



class BShell(cmd.Cmd):
    intro = "Welcome to BShell! Enter help or ? for see command list.\n"
    prompt = "BShellUser> "

    def do_exit(self, arg):
        'Выход из BShell'
        print("Exit From BShell... ")
        return True
        
    def do_goto(self, path):
        'Переход в указанную папку: переход [путь]'
        try:
            os.chdir(path)
            print(f"Current Directory: {os.getcwd()}")
        except Exception as e:
            print(f"Error: {e}")

    def do_show_files(self, arg):
        'Показать содержимое папки'
        print("\n".join(os.listdir(os.getcwd())))

    def do_create_dir(self, dirname):
        'Создать новую папку: create_dir [имя_папки]'
        try:
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_dir(self, dirname):
        'Удалить папку: delete_dir [имя_папки]'
        try:
            os.rmdir(dirname)
            print(f"Directory '{dirname}' was deleted.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def do_create_file(self, filename):
        'Создать пустой файл: создать_файл [имя_файла]'
        try:
            with open(filename, 'w') as f:
                pass
            print(f"File '{filename}' was created.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_file(self, filename):
        'Удалить файл: удалить_файл [имя_файла]'
        try:
            os.remove(filename)
            print(f"File '{filename}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")

    def do_change_name(self, args):
        'Переименовать файл: переименовать_файл [текущий_имя] [новое_имя]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"File '{old_name}' was changed in '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_run_file(self, filename):
        'Запустить Python файл: запустить_файл [имя_файла]'
        try:
            subprocess.run(['python', filename])
        except Exception as e:
            print(f"Error: {e}")
    
        
    def do_read_file(self, filename):
        'Прочитать файл: чтение_файла [имя_файла]'
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Error: {e}")

    def do_write_file(self, args):
        'Записать в файл: запись_в_файл [имя_файла] [текст]'
        try:
            filename, text = args.split(maxsplit=1)
            with open(filename, 'a') as f:
                f.write(text + '\n')
            print(f"Text was writed in file '{filename}'")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    BShell().cmdloop()