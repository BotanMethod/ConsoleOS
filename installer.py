import os
import shutil
import json
import importlib
import sys
import subprocess
import time

def check_dependencies():
    dependencies = ["psutil", "getpass", 'pygame', 'shutil']
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            print(f"Установка {dep}...")
            subprocess.run([sys.executable, "-m", "pip", "install", dep])

check_dependencies()

def create_directory_structure(base_path):
    dirs = [
        os.path.join(base_path, "ConsoleOS"),
        os.path.join(base_path, "ConsoleOS", "System"),
        os.path.join(base_path, "ConsoleOS", "Configuration"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    return os.path.join(base_path, "ConsoleOS")

def copy_files(src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def main():
    install_dir = input("Enter installation path (default: current dir): ") or "."
    base_path = create_directory_structure(install_dir)
    
    # Копируем исходные файлы
    copy_files("src/System", os.path.join(base_path, "System"))
    copy_files("src/Configuration", os.path.join(base_path, "Configuration"))
    shutil.copy("src/kernel.py", base_path)
    
    print(f"ConsoleOS successfully installed in {base_path}")
    print('Installer will be closed automatically in 5 seconds')
    time.sleep(5)

if __name__ == "__main__":
    main()
