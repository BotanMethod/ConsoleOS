from datetime import datetime
from src.utils.logger import AppLogger

class Clock:
    def __init__(self):
        self.logger = AppLogger("CLOCK")

    def get_time(self):
        now = datetime.now()
        self.logger.info("Time requested")
        self.logger.info(now.strftime("%H:%M:%S %d/%m/%Y"))
        