from src.utils.logger import SystemLogger
from time import sleep
from os import system

class MemoryManager:
    def __init__(self):
        self.logger = SystemLogger("MEMORY")
        self.syslogger = SystemLogger("SYSTEM")
        self.allocated = False

    def allocate(self):
        try:
            self.logger.info("Allocating 512MB system memory")
            self.syslogger.info("Loading assets...")
            sleep(2)
            self.syslogger.success("Assets loaded. System ready to work. Wait few seconds")
            sleep(5)
            system('cls')
            self.allocated = True
        except Exception as e:
            self.logger.error(f"Memory allocation failed: {str(e)}")
            raise