from src.utils.logger import SystemLogger

class InputDriver:
    def __init__(self):
        self.logger = SystemLogger("INPUT")

    def get(self):
        try:
            return input("\033[94muser@python-os>\033[0m ")
        except Exception as e:
            self.logger.error(f"Input error: {str(e)}")
            raise