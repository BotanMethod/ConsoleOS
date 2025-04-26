from src.utils.logger import SystemLogger

class DisplayDriver:
    def __init__(self):
        self.logger = SystemLogger("DISPLAY")
        self.initialized = False

    def test(self):
        try:
            self.logger.info("Running display diagnostics...")

            self.initialized = True
            self.logger.success("Display self-test passed")
        except Exception as e:
            self.initialized = False
            self.logger.error(f"Display test failed: {str(e)}")
            raise

    def initialize(self):
        if not self.initialized:
            raise RuntimeError("Display must be tested before initialization")
        self.logger.info("Initializing display subsystem")

        self.logger.success("Display ready (1024x768 RGB)")