import os
import cmd
import time
import subprocess

OSinfo = os.name


print("Loading ConsoleOS...")
time.sleep(1)
print("Successfully loaded ConsoleOS / Booting system...")
time.sleep(1)

print("░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗░█████╗░░██████╗")
time.sleep(0.2)
print("██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔════╝")
time.sleep(0.2)
print("██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░██║░░██║╚█████╗░")
time.sleep(0.2)
print("██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░██║░░██║░╚═══██╗")
time.sleep(0.2)
print("╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗╚█████╔╝██████╔╝")
time.sleep(0.2)
print("░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝░╚════╝░╚═════╝░")
time.sleep(3)

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

class Consoleplatform(cmd.Cmd):
    intro = print("ConsoleOS | 1.0.1 [BUGFIX]")
    print("OpenSource & Free")
    time.sleep(1)
    print(" ")
    prompt = f"ConsoleOS.exe\ConsoleOS> ^ "

    def do_exit(self, arg):
        'Exit from ConsoleOS'
        print("Exiting From ConsoleOS... ")
        time.sleep(3)
        return True
    
    def do_info(self, arg):
        'Shows info about ConsoleOS'
        print("INFO:")
        print("Engine: ConsolePlatform, Cmd")
        print("[Your] OS Base: " + OSinfo) 
        print("Version: 1.0.1 [BUGFIX]")
        print("Bugfix: [YES]")
        print("Beta: [NO]")
        print("Alpha: [NO]")
        print("Pre-release: [NO]")

    def do_cln(self, arg):
        'Cleans the Console'
        try:
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) 
        except Exception as e:
            print(f"Error: {e}")
    
    def do_emoji(self, arg):
        'Prints text emoji in Console | Changeable'
        print(":)")
    
    def do_say(self, arg):
        'Prints your text'
        text = input("Enter text | ")
        print(text)
        
    def do_goto(self, path):
        'Go to the specified folder: goto [path]'
        try:
            os.chdir(path)
            print(f"Current Directory: {os.getcwd()}")
        except Exception as e:
            print(f"Error: {e}")
    
    def do_show_files(self, arg):
        'Show folder contents'
        print("\n".join(os.listdir(os.getcwd())))

    def do_create_dir(self, dirname):
        'Create a new folder: create_dir [folder name]'
        try:
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        except Exception as e:
            print(f"Error: {e}")
    
    def do_delete_dir(self, dirname):
        'Delete folder: delete_dir [folder_name]'
        try:
            os.rmdir(dirname)
            print(f"Directory '{dirname}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_create_file(self, filename):
        'Create an empty file: create_file [file_name]'
        try:
            with open(filename, 'w') as f:
                pass
            print(f"File '{filename}' was created.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_file(self, filename):
        'Delete file: delete_file [file_name]'
        try:
            os.remove(filename)
            print(f"File '{filename}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")

    def do_change_name(self, args):
        'Rename the file: rename the file [current name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"File '{old_name}' was renamed to '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_runpy(self, filename):
        'Run Python file: run_file [file_name]'
        try:
            subprocess.run(['python', filename])
        except Exception as e:
            print(f"Error: {e}")

    def do_run(self, filename):
        'Run .exe file: run [file_name]'
        try:
            subprocess.run([filename])
        except Exception as e:
            print(f"Error: {e}")
    
    def do_read_file(self, filename):
        'Read file: read_file [file_name]'
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Error: {e}")

    def do_write_file(self, args):
        'Write to file: write to file [file_name] [text]'
        try:
            filename, text = args.split(maxsplit=1)
            with open(filename, 'a') as f:
                f.write(text + '\n')
            print(f"Text was writed in file '{filename}'")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    Consoleplatform().cmdloop()
