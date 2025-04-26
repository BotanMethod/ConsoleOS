import json
from pathlib import Path
from src.utils.logger import SystemLogger
import datetime
import os

class FileSystem:
    def __init__(self):
        self.logger = SystemLogger("FS")
        self.root = Path(__file__).parent.parent.parent / "vfs"
        self.meta_file = self.root / ".meta"

    def create(self, path, content=""):
        full_path = self.root / path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w') as f:
            f.write(content)
        
        self._update_metadata(path)
        self.logger.info(f"Created file: {path}")

    def _update_metadata(self, path):
        meta = {}
        if self.meta_file.exists():
            with open(self.meta_file) as f:
                meta = json.load(f)
        
        meta[path] = {
            'size': os.path.getsize(self.root / path),
            'created': str(datetime.now())
        }
        
        with open(self.meta_file, 'w') as f:
            json.dump(meta, f)