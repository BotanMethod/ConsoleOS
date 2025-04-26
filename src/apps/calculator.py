from src.utils.logger import AppLogger

class Calculator:
    def __init__(self):
        self.logger = AppLogger("CALC")

    def evaluate(self, expr):
        try:
            result = eval(expr)
            self.logger.info(f"{expr} = {result}")
            return result
        except Exception as e:
            self.logger.error(f"Calculation error: {str(e)}")
            raise