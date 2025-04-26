import os
import time
import subprocess
import threading
import pygame
from cmd import Cmd
from src.utils.logger import AppLogger

class MusicPlayer(Cmd):
    
    def __init__(self):
        super().__init__()
        self.logger = AppLogger("MUSIC")
        self.is_playing = False
        self.current_thread = None
        pygame.mixer.init()
        self.prompt = "\nMusic Player > "  

    def do_play(self, filename):
        'Plays a music file: play [file_name]'
        if self.is_playing:
            print("Music is already playing. Please stop it before playing a new file.")
            return
        pass

        self.current_thread = threading.Thread(target=self._play_music, args=(filename,))
        self.current_thread.start()

    def _play_music(self, filename):
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            self.is_playing = True
            self.logger.info(f"Playing: {filename}")

            audio = pygame.mixer.Sound(filename)
            duration = audio.get_length()
            start_time = time.time()

            while pygame.mixer.music.get_busy():
                elapsed = time.time() - start_time
                elapsed_str = f"{int(elapsed//60):02}:{int(elapsed%60):02}"
                total_str = f"{int(duration//60):02}:{int(duration%60):02}"
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                print(f"\rPlaying... {elapsed_str} / {total_str}", end="")
                time.sleep(1)

            print()
            self.is_playing = False
        except Exception as e:
            self.logger.error(str(e))
            self.is_playing = False

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
        'Exits the music player'
        pygame.mixer.quit()
        print("Exiting music player.")
        return True