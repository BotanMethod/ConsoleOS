from src.system.filesystem import FileSystem
from src.utils.logger import AppLogger

class TextEditor:
    def __init__(self):
        self.logger = AppLogger("TEXT")
        self.fs = FileSystem()
        self.buffer = []
        self.filename = None

    def open(self, filename):
        try:
            with open(self.fs.root / filename, 'r') as f:
                self.buffer = f.readlines()
            self.filename = filename
            return True
        except FileNotFoundError:
            return False

    def save(self):
        if not self.filename:
            raise ValueError("No file opened")
        
        with open(self.fs.root / self.filename, 'w') as f:
            f.writelines(self.buffer)

    def interactive(self):
        print("Enter text (Ctrl+D to save):")
        while True:
            try:
                line = input()
                self.buffer.append(line + '\n')
            except EOFError:
                break