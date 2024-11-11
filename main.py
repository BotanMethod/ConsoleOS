import os
import cmd
import time
import subprocess
import getpass
from shutil import copytree, rmtree
import psutil
import random

version = str('1.2.0')
versionyear = str('1.2.0')

# Author: UntitledCatDeveloper, also known as BotanMethod

class Editor:
    def __init__(self):
        Editor.start = True
        Editor.text = []
        Editor.line = 1
        
    
    def editor_on(self):
        while Editor.editor_on:
            print(" ")
            text = input(f"{self.line}:  ")
            if text == "SAVEFILE":
                Editor.start = False
                Editor.save_text(self)
                print(" ")
                break
            else:
                Editor.text.append(text)
                Editor.line += 1 

    
    def save_text(self):
        fn = input("Save as (Name): ")
        fe = input("Save as (Extension) (Ex. [.py .txt .html]): ")
        with open(f"{fn}.{fe}", 'w') as f:
            for line in Editor.text:
                f.write(line + '\n')
        print("Code was saved successfully!")
        print("Saved in: ", os.path.abspath(f'{fn}.{fe}'))
        

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
print("CONSOLEOS░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗░█████╗░░██████╗CONSOLEOS")
time.sleep(0.1)
print("CONSOLEOS██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔════╝CONSOLEOS")
time.sleep(0.1)
print("CONSOLEOS██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░██║░░██║╚█████╗░CONSOLEOS")
time.sleep(0.1)
print("CONSOLEOS██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░██║░░██║░╚═══██╗CONSOLEOS")
time.sleep(0.1)
print("CONSOLEOS╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗╚█████╔╝██████╔╝CONSOLEOS")
time.sleep(0.1)
print("CONSOLEOS░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝░╚════╝░╚═════╝░CONSOLEOS")
time.sleep(3)
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

class Consoleplatform(cmd.Cmd):
    intro = f"Console Operating System. Full Version. [{version}], {versionyear}\n "
    time.sleep(1.5)
    prompt = f"💠 ConsoleOS | 🖥️ User: [{getpass.getuser()}] | 📂 [{os.getcwd()}] / "
    
    def __init__(self):
        super().__init__()
    
    def do_calc(self, arg):
        'Starts the calculator'
        while True:
            try:
                num1 = float(input("Enter first number (or 's' for stop calculating) | "))
                operation = input("Enter operation (+, -, *, /) | ")
                num2 = float(input("Enter second number | "))

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        self.show_error("Error: you tried to divide by zero >:(")
                        continue
                    result = num1 / num2
                else:
                    self.show_error("Error: invalid operation >:(")
                    continue

                print(f"Result: {result}")

            except ValueError:
                if input("Invalid input. Do you want to exit? [Y/N] ").lower() == 'y':
                    break

    def do_exit(self, arg):
        'Exits from ConsoleOS'
        a = input("Are you sure you want to exit ConsoleOS? [Y/N] | ")
        if a.lower() == "y":
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            print("Preparing ConsoleOS for exit...")
            time.sleep(3)
            return True

    def do_info(self, arg):
        'Shows info about ConsoleOS'
        print("Information about ConsoleOS from Developer:")
        print(f"[Your] OS Base: {os.name}") 
        print("Version: 1.2, 2024")
        print(f"Username: {getpass.getuser()}")
        print("Developer: BDevelopment")

    def do_shutdown(self, arg):
        'Shuts down your device'
        b = input("Are you sure you want to shut down device? [Y/N] | ")
        if b.lower() == "y":
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            time_input = int(input("Enter time in seconds for shutdown: "))
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            print("Shutting down your computer...")
            time.sleep(1)
            os.system(f"shutdown /s /t {time_input}")
        else:
            print("Shutdown cancelled.")
            
    def do_reboot(self, arg):
        'Reboots your device'
        c = input("Are you sure you want to reboot device? [Y/N] | ")
        if c.lower() == "y":
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            time_input = int(input("Enter time in seconds for reboot: "))
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            print("Rebooting your computer...")
            time.sleep(1)
            os.system(f"shutdown /r /t {time_input}")
        else:
            print("Reboot cancelled.")
            
    def do_cln(self, arg):
        'Cleans the Console'
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    def do_echo(self, text):
        'Prints your text: echo [text]'
        print(text)
        
    def do_util(self, utilname):
        'Runs util programs: util [util_name]'
        try:
            subprocess.run(['python', f'system/{utilname}.py'])  
        except Exception as e:
            print(f"Error: {e}")
            
    def do_cd(self, path):
        'Moves to the specified directory: cd [path]'
        try:
            os.chdir(path)
            print(" ")
            self.prompt = f"💠 ConsoleOS | 🖥️ User: [{getpass.getuser()}] | 📂 [{os.getcwd()}] / "
        except Exception as e:
            print(f"Error: {e}")
            
    def do_ls(self, arg):
        "Shows folder's contents"
        print("\n".join(os.listdir(os.getcwd())))
        
    def do_mkdir(self, dirname):
        'Creates a new directory: create_dir [dir_name]'
        try:
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rmdir(self, dirname):
        'Deletes directory: delete_dir [dir_name]'
        try:
            rmtree(dirname)
            print(f"Directory '{dirname}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rdir(self, args):
        'Renames the directory: rdir [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"Directory '{old_name}' was renamed to '{new_name}' ")
        except Exception as e:
            print(f'Error: {e}')
            
    def do_mkfile(self, filename):
        'Creates an empty file: create_file [file_name]'
        try:
            with open(filename, 'w') as f:
                pass
            print(f"File '{filename}' was created.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_edit(self, filename):
        'Edits file: edit [file_name]'
        try:
            subprocess.run(['notepad.exe', filename])
        except Exception as e:
            print(f"Error: {e}")
        
    def do_code(self, args):
        'Edits file: code [file_name]'
        try:
            Editor.editor_on(self=Editor)
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rmfile(self, filename):
        'Deletes file: delete_file [file_name]'
        try:
            os.remove(filename)
            print(f"File '{filename}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rnfile(self, args):
        'Renames the file: change_name [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"File '{old_name}' was renamed to '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rfile(self, filename):
        'Reads file: read_file [file_name]'
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Error: {e}")
            

    def do_wfile(self, args):
        'Writes to file: write_file [file_name] [text]'
        try:
            filename, text = args.split(maxsplit=1)
            with open(filename, 'a') as f:
                f.write(text + '\n')
            print(f"Text was written in file '{filename}'")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_find(self, filename):
        'Finds for a file in the current directory: search_file [file_name]'
        found = False
        for root, dirs, files in os.walk(os.getcwd()):
            if filename in files:
                print(f"Found: {os.path.join(root, filename)}")
                found = True
        if not found:
            print("File not found.")
            
    def do_tasklist(self, args):
        'Shows all running processes: tasklist'
        for process in psutil.process_iter(['pid', 'name']):
            print(f"{process.info['pid']}: {process.info['name']}")
            
    def do_taskkill(self, arg):
        'Terminates a process by PID or name: taskkill [pid | process_name]'
        try:
            if arg.isdigit():
                os.kill(int(arg), 9)
                print(f"Process {arg} terminated.")
            else:
                for proc in psutil.process_iter():
                    if proc.name() == arg:
                        proc.kill()
                        print(f"Process '{arg}' terminated.")
                        return
                print(f"No process found with the name '{arg}'.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_resmon(self, args):
        'Shows CPU and memory usage: resmon'
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")
        time.sleep(1)
        
    def do_chkdsk(self, arg):
        'Shows information about current disk'
        usage = psutil.disk_usage('/')
        print(f"Total: {usage.total / (1024**3):.2f} GB")
        print(f"Used: {usage.used / (1024**3):.2f} GB")
        print(f"Free: {usage.free / (1024**3):.2f} GB")
            
    def do_runpy(self, filename):
        'Runs Python Script files: runpy [file_name]'
        try:
            subprocess.run(['python', filename])
        except Exception as e:
            print(f"Error: {e}")

    def do_run(self, filename):
        'Runs .exe files: run [file_name]'
        try:
            subprocess.run([filename])
        except Exception as e:
            print(f"Error: {e}")

    def do_date(self, arg):
        'Shows the current date and time'
        print("Current date and time:", time.strftime("%Y-%m-%d %H:%M:%S"))

editor = Editor()

if __name__ == '__main__':
    Consoleplatform().cmdloop()
