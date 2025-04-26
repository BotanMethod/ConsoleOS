import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from src.kernel.boot import Bootloader

if __name__ == "__main__":
    boot = Bootloader()
    kernel = boot.load_kernel()
    kernel.initialize()
