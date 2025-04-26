import os
from pathlib import Path
from src.utils.logger import SystemLogger

class StorageDriver:
    def __init__(self):
        self.logger = SystemLogger("STORAGE")
        self.vfs_path = Path(__file__).parent.parent.parent / "vfs"
        self.mounted = False

    def test(self):
        test_file = self.vfs_path / ".storage_test"
        try:
            test_file.touch()
            test_file.unlink()
        except Exception as e:
            raise RuntimeError(f"Storage test failed: {str(e)}")

    def mount(self):
        if not self.vfs_path.exists():
            self.vfs_path.mkdir()
            self.logger.info(f"Created VFS at {self.vfs_path}")
        
        self.mounted = True
        self.logger.success("Mounted virtual filesystem")