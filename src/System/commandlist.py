import os
import time
import subprocess
import getpass
from shutil import rmtree
import psutil
import pygame
import threading

version = '1.3.1'
versionyear = '2025'

class MusicPlayer:
    intro = 'Welcome to the Music Player. Type help or ? to list commands.'
    prompt = f'[{os.getcwd()}]> '

    def __init__(self):
        super().__init__()
        self.is_playing = False
        self.current_thread = None 
        pygame.mixer.init()

    def do_cd(self, path):
        'Moves to the specified directory: cd [path]'
        try:
            os.chdir(path)
            print(" ")
            self.prompt = f"[{os.getcwd()}]> "
        except Exception as e:
            print(f"Error: {e}")
            
    def do_ls(self, arg):
        "Shows folder's contents: ls"
        print("\n".join(os.listdir(os.getcwd())))

    def play_music(self, filename):
        'Вспомогательный метод для воспроизведения музыки в отдельном потоке'
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            self.is_playing = True
            print(f"Playing: {filename}")

            # Получаем длительность трека
            audio = pygame.mixer.Sound(filename)
            duration = audio.get_length()  # Длительность в секундах
            start_time = time.time()

            # Ожидание, пока музыка играет
            while pygame.mixer.music.get_busy():
                elapsed_time = time.time() - start_time
                elapsed_minutes = int(elapsed_time // 60)
                elapsed_seconds = int(elapsed_time % 60)
                total_minutes = int(duration // 60)
                total_seconds = int(duration % 60)

                # Отображаем таймлайн
                subprocess.run('cls')
                print(f"\rPlaying... {elapsed_minutes:02}:{elapsed_seconds:02} / {total_minutes:02}:{total_seconds:02}", end="")
                time.sleep(1)

            print()  # Для новой строки после завершения воспроизведения
            self.is_playing = False

        except Exception as e:
            print(f"Error: {e}")
            self.is_playing = False

    def do_play(self, filename):
        'Plays a music file: play [file_name]'
        if self.is_playing:
            print("Music is already playing. Please stop it before playing a new file.")
            return

        self.current_thread = threading.Thread(target=self.play_music, args=(filename,))
        self.current_thread.start()

    def do_stop(self, arg):
        'Stops the music: stop'
        try:
            pygame.mixer.music.stop()
            self.is_playing = False
            print("Music stopped.")
        except Exception as e:
            print(f"Error: {e}")

    def do_pause(self, arg):
        'Pauses the music: pause'
        try:
            pygame.mixer.music.pause()
            print("Music paused.")
        except Exception as e:
            print(f"Error: {e}")

    def do_unpause(self, arg):
        'Unpauses the music: unpause'
        try:
            pygame.mixer.music.unpause()
            print("Music unpaused.")
        except Exception as e:
            print(f"Error: {e}")

    def do_volume_up(self, arg):
        'Increases the volume: volume_up'
        current_volume = pygame.mixer.music.get_volume()
        new_volume = min(current_volume + 0.1, 1.0)
        pygame.mixer.music.set_volume(new_volume)
        print(f"Volume increased to {new_volume:.1f}")

    def do_volume_down(self, arg):
        'Decreases the volume: volume_down'
        current_volume = pygame.mixer.music.get_volume()
        new_volume = max(current_volume - 0.1, 0.0)
        pygame.mixer.music.set_volume(new_volume)
        print(f"Volume decreased to {new_volume:.1f}")

    def do_exit(self, arg):
        'Exits the music player: exit'
        print("Exiting music player.")
        return True  

class ConsoleCommands:
    """Класс со всеми командами для консоли"""
    def do_Music_player(self, arg):
        'Opens the music player: Music_player'
        print("Starting Music Player...")
        MusicPlayer().cmdloop()  
    
    def do_calc(self, arg):
        'Starts the calculator: calc'
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
                    print("Error: invalid operation >:(")
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
        print(f"Version: {version}, {versionyear}")
        print(f"Username: {getpass.getuser()}")
        print("Developer: BDevelopment")
        print('''              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +newgenM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@42- XM@X;. -+bigupdateM@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    new+..%#$.
 /consoleos/                  update =;
  /%+%$XHH@$=              , .inMMM@MX,
   .=botan---.           -%H.,??/??MX,
   .%methodHHXX$$$%+- .:$MMX ???@MM%.
     =абаюнда@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#CONSOLEOS =,
               =++%%%%+/:-.''')

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
            
    def do_cd(self, path):
        'Moves to the specified directory: cd [path]'
        try:
            os.chdir(path)
            print(" ")
            self.prompt = f"[COS] ConsoleOS / User: [{getpass.getuser()}] / Dir: [{os.getcwd()}] $ "
        except Exception as e:
            print(f"Error: {e}")
            
    def do_ls(self, arg):
        "Shows folder's contents: ls"
        print("\n".join(os.listdir(os.getcwd())))
        
    def do_mkdir(self, dirname):
        'Creates a new directory: mkdir [dir_name]'
        try:
            os.makedirs(dirname)
            print(f"Directory '{dirname}' was created.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rmdir(self, dirname):
        'Deletes directory: rmdir [dir_name]'
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
        'Creates an empty file: mkfile [file_name]'
        try:
            with open(filename, 'w') as f:
                pass
            print(f"File '{filename}' was created.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_edit(self, filename):
        'Edits file with notepad: edit [file_name]'
        try:
            subprocess.run(['notepad.exe', filename])
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rmfile(self, filename):
        'Deletes file: rmfile [file_name]'
        try:
            os.remove(filename)
            print(f"File '{filename}' was deleted.")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rnfile(self, args):
        'Renames the file: rnfile [cur_name] [new_name]'
        try:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
            print(f"File '{old_name}' was renamed to '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_rfile(self, filename):
        'Reads file: rfile [file_name]'
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
            print(f"Error: {e}")
            
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
            print(f"Error: {e}")

    def do_run(self, filename):
        'Runs .exe files: run [file_name]'
        try:
            subprocess.run([filename])
        except Exception as e:
            print(f"Error: {e}")

    def do_date(self, arg):
        'Shows the current date and time: date'
        print("Current date and time:", time.strftime("%Y-%m-%d %H:%M:%S"))
