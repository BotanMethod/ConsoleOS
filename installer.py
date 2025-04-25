import os
import shutil
import json

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

def create_config(config_path):
    config = {
        "version": "1.3.0 [F]",
        "versionyear": "2025"
    }
    with open(os.path.join(config_path, "cosconfig.json"), 'w') as f:
        json.dump(config, f, indent=4)

def main():
    install_dir = input("Enter installation path (default: current dir): ") or "."
    base_path = create_directory_structure(install_dir)
    
    # Копируем исходные файлы
    copy_files("src/System", os.path.join(base_path, "System"))
    copy_files("src/Configuration", os.path.join(base_path, "Configuration"))
    shutil.copy("src/kernel.py", base_path)
    
    # Создаем конфиг
    create_config(os.path.join(base_path, "Configuration"))
    
    print(f"ConsoleOS успешно установлен в {base_path}")

if __name__ == "__main__":
    main()
