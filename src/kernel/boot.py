import psutil
import traceback
from pathlib import Path
from src.utils.logger import SystemLogger
from src.drivers.storage import StorageDriver
from src.drivers.display import DisplayDriver
from src.drivers.input import InputDriver
import sys
from src.kernel.core import Kernel

class Bootloader:
    def __init__(self):
        self.logger = SystemLogger("BOOT")
        self.root_path = Path(__file__).parent.parent.parent
        self.errors = []
        

        self.drivers = {
            'display': DisplayDriver(),
            'storage': StorageDriver(),
            'input': InputDriver()
        }

    def _check_hardware(self):
        checks = {
            'memory': self._check_memory,
            'cpu': self._check_cpu,
            'display': lambda: self.drivers['display'].test(),
            'storage': lambda: self.drivers['storage'].test()
        }

        for name, check in checks.items():
            try:
                check()
                self.logger.success(f"{name.upper()} check passed")
            except Exception as e:
                self._log_error(e, name)
                
    def _check_memory(self):
        mem = psutil.virtual_memory()
        if mem.total < 1_073_741_824:
            raise MemoryError(f"RAM: {mem.total//1024**2}MB < 1024MB")

    def _check_cpu(self):
        if psutil.cpu_count() < 2:
            raise RuntimeError(f"Cores: {psutil.cpu_count()} < 2")

    def _log_error(self, error, component):
        tb = traceback.extract_tb(error.__traceback__)[-1]
        self.errors.append({
            'component': component,
            'type': type(error).__name__,
            'msg': str(error),
            'file': str(Path(tb.filename).relative_to(self.root_path)),
            'line': tb.lineno
        })

    def load_kernel(self):
        self.logger.info("Initializing hardware...")
        self._check_hardware()
        
        if self.errors:
            self._print_errors()
            sys.exit(1)
            
        return Kernel(
            display=self.drivers['display'], 
            storage=self.drivers['storage']   
    )

    def _print_errors(self):
        print("\n\033[91mHARDWARE FAILURE REPORT:\033[0m")
        for error in self.errors:
            print(f"""
  File: {error['file']}
  Line: {error['line']}
  Error: {error['type']} - {error['msg']}
  Code: \033[93m{error['code']}\033[0m
            """)