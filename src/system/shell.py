import cmd
import os
import subprocess
import time
import psutil
import colorama
from src.apps.calculator import Calculator
from src.apps.text_editor import TextEditor
from src.apps.clock import Clock
from src.drivers.input import InputDriver
from src.utils.logger import SystemLogger
from src.apps.music_player import MusicPlayer
from src.config.version import versionapp
from src.config.user import user
from src.system.filesystem import FileSystem

class Shell(cmd.Cmd):
    prompt = f"{colorama.Style.BRIGHT}{colorama.Back.GREEN}{colorama.Fore.WHITE}cos@{user}{colorama.Back.RESET}{colorama.Fore.RESET} / {colorama.Style.BRIGHT}{colorama.Back.CYAN}{colorama.Fore.WHITE}{os.getcwd()}{colorama.Fore.RESET}{colorama.Back.RESET} $ "
    intro = f"Console Operating System / {versionapp}"
    
    def __init__(self):
        super().__init__()
        self.logger = SystemLogger("SHELL")
        self.promplogger = SystemLogger("PROMPT")
        self.calc = Calculator()
        self.editor = TextEditor()
        self.clock = Clock()
        
    def do_cd(self, path):
        'Moves to the specified directory: cd [path]'
        try:
            os.chdir(path)
            self.prompt = f"{colorama.Back.GREEN}{colorama.Fore.WHITE}cos@{user}{colorama.Back.RESET}{colorama.Fore.RESET} / {colorama.Back.CYAN}{colorama.Fore.WHITE}{os.getcwd()}{colorama.Fore.RESET}{colorama.Back.RESET} $ "
        except Exception as e:
            self.logger.error(e)
            
    def do_Music_player(self, arg):
        'Opens the music player: Music_player'
        print("Starting Music Player...")
        MusicPlayer().cmdloop()  
    
    def do_calc(self, arg):
        'Starts the calculator: calc'
        self.calc.evaluate(arg)
    
    def do_exit(self, arg):
        'Exits from ConsoleOS'
        a = input("Are you sure you want to exit ConsoleOS? [Y/N] | ") 
        if a.lower() == "y":
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            self.logger.info("Preparing ConsoleOS for exit...")
            time.sleep(3)
            return True
        
    def do_info(self, arg):
        'Shows info about ConsoleOS'
        self.logger.info("Information about ConsoleOS and your Device")
        self.logger.info(f"[Your] OS Base: {os.name}") 
        self.logger.info(f"Version: {versionapp}")
        self.logger.info(f"Username: {user}")
        self.logger.info("Developer: UntitledCatDev (a.k.a. BotanMethod)")
        self.logger.info(f"---Idk what paste there---")

    def do_shutdown(self, time):
        'Shuts down your device'
        b = input("Are you sure you want to shut down device? [Y/N] | ")
        if b.lower() == "y":
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            print("Shutting down your computer...")
            time.sleep(1)
            os.system(f"shutdown /s /t {time}")
        else:
            print("Shutdown cancelled.")
            
    def do_reboot(self, time):
        'Reboots your device: reboot [time]'
        c = input("Are you sure you want to reboot device? [Y/N] | ")
        if c.lower() == "y":
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            print("Rebooting your computer...")
            time.sleep(1)
            os.system(f"shutdown /r /t {time}")
        else:
            print("Reboot cancelled.")
            
    def do_cln(self, arg):
        'Cleans the Console: cln'
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    def do_echo(self, text):
        'Prints your text: echo [text]'
        print(text)
            
    def do_ls(self, arg):
        "Shows folder's contents: ls"
        print("\n".join(os.listdir(os.getcwd())))
        
    def do_mkdir(self, dirname):
        'Creates a new directory: mkdir [dir_name]'
        try:
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        except Exception as e:
            self.logger.error(e)
            
    def do_rmdir(self, dirname):
        'Deletes directory: rmdir [dir_name]'
        try:
            subprocess.rmtree(dirname)
            print(f"Directory '{dirname}' was deleted.")
        except Exception as e:
            self.logger.error(e)
            
    def do_rdir(self, args):
        'Renames the directory: rdir [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"Directory '{old_name}' was renamed to '{new_name}' ")
        except Exception as e:
            self.logger.error(e)
            
    def do_mkfile(self, filename):
        'Creates an empty file: mkfile [file_name]'
        try:
            with open(filename, 'w') as f:
                pass
            print(f"File '{filename}' was created.")
        except Exception as e:
            self.logger.error(e)
            
    def do_edit(self, filename):
        'Edits file with notepad: edit [file_name]'
        try:
            subprocess.run(['notepad.exe', filename])
        except Exception as e:
            self.logger.error(e)
        
            
    def do_rmfile(self, filename):
        'Deletes file: rmfile [file_name]'
        try:
            os.remove(filename)
            print(f"File '{filename}' was deleted.")
        except Exception as e:
            self.logger.error(e)
            
    def do_rnfile(self, args):
        'Renames the file: rnfile [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"File '{old_name}' was renamed to '{new_name}'")
        except Exception as e:
            self.logger.error(e)
            
    def do_rfile(self, filename):
        'Reads file: rfile [file_name]'
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except Exception as e:
            self.logger.error(e)
            

    def do_wfile(self, args):
        'Writes to file: write_file [file_name] [text]'
        try:
            filename, text = args.split(maxsplit=1)
            with open(filename, 'a') as f:
                f.write(text + '\n')
            print(f"Text was written in file '{filename}'")
        except Exception as e:
            self.logger.error(e)
            
    def do_find(self, filename):
        'Finds for a file in the current directory: find [file_name]'
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
            self.logger.error(e)
            
    def do_resmon(self, args):
        'Shows CPU and memory usage: resmon'
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")
        time.sleep(1)
        
    def do_chkdsk(self, arg):
        'Shows information about current disk: chkdsk'
        usage = psutil.disk_usage('/')
        print(f"Total: {usage.total / (1024**3):.2f} GB")
        print(f"Used: {usage.used / (1024**3):.2f} GB")
        print(f"Free: {usage.free / (1024**3):.2f} GB")
            
    def do_runpy(self, filename):
        'Runs Python Script files: runpy [file_name]'
        try:
            subprocess.run(['python', filename])
        except Exception as e:
            self.logger.error(e)

    def do_run(self, filename):
        'Runs .exe files: run [file_name]'
        try:
            subprocess.run([filename])
        except Exception as e:
            self.logger.error(e)

    def do_date(self, arg):
        'Shows the current date and time: date'
        Clock.get_time(self)
