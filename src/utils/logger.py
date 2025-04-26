import sys
import traceback
from datetime import datetime
from pathlib import Path
from colorama import Fore, Style

class SystemLogger:
    def __init__(self, tag):
        self.tag = tag
        self.root = Path(__file__).parent.parent.parent

    def _format(self, level, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        return f"{Fore.CYAN}[{timestamp}]{Style.RESET_ALL} [{self.tag}] {level}: {msg}"

    def info(self, msg):
        print(self._format(f"{Fore.GREEN}INFO{Style.RESET_ALL}", msg))

    def error(self, msg):
        exc_type, exc_value, tb = sys.exc_info()
        frame = traceback.extract_tb(tb)[-1] if tb else None
        location = f"{Path(frame.filename).relative_to(self.root)}:{frame.lineno}" if frame else ""
        print(self._format(f"{Fore.LIGHTRED_EX}ERROR{Style.RESET_ALL}", f"{msg} @ {location}"))

    def critical(self, msg):
        print(self._format(f"{Fore.RED}{Style.BRIGHT}CRITICAL{Style.RESET_ALL}", msg))

    def success(self, msg):
        print(self._format(f"{Fore.CYAN}SUCCESS{Style.RESET_ALL}", msg))

class AppLogger(SystemLogger):
    def warning(self, msg):
        print(self._format(f"{Fore.YELLOW}WARN{Style.RESET_ALL}", msg))