import cmd
import time
import getpass
import os
from System.commandlist import ConsoleCommands, MusicPlayer
from System.commandlist import version, versionyear

class ConsoleOS(cmd.Cmd, ConsoleCommands):
    def __init__(self):
        super().__init__()
        self.intro = self.get_intro()
        self.update_prompt()
        
    version = version
    versionyear = versionyear
    
    def get_intro(self):
        return (
            f"Console Operating System. [{self.version}], {self.versionyear}\n"
            "Type 'help' for available commands.\n"
        )
    
    def update_prompt(self):
        self.prompt = (
            f"[COS] ConsoleOS / User: [{getpass.getuser()}] "
            f"/ Dir: [{os.getcwd()}] # "
        )
    
    def do_Music_player(self, arg):
        'Opens the music player: Music_player'
        print("Starting Music Player...")
        MusicPlayer().cmdloop()

if __name__ == '__main__':
    ConsoleOS().cmdloop()
