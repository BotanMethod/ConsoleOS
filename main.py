import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from src.kernel.boot import Bootloader
from src.utils.logger import SystemLogger

logger = SystemLogger("CORE")

if __name__ == "__main__":
    os.system('cls')
    logger.info("Starting ConsoleOS...")
    try:
        boot = Bootloader()
        kernel = boot.load_kernel()
        kernel.initialize()
    except Exception as e:
        logger.critical(f"Boot failed: {str(e)}")
        sys.exit(1)
