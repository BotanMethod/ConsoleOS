from src.system.shell import Shell
from src.drivers.display import DisplayDriver
from src.drivers.storage import StorageDriver
from src.system.memory import MemoryManager
from src.utils.logger import SystemLogger

class Kernel:
    def __init__(self, display, storage):  # Добавляем явные параметры
        self.logger = SystemLogger("KERNEL")
        self.display_driver = display
        self.storage_driver = storage
        self.memory_manager = MemoryManager()
        self.shell = Shell()

    def initialize(self):
        self.logger.info("Loading kernel modules")
        try:
            self.display_driver.initialize()
            self.storage_driver.mount()
            self.memory_manager.allocate()
            
            self.shell.cmdloop()
        except Exception as e:
            self.logger.critical(f"Kernel panic: {str(e)}")
            raise
        