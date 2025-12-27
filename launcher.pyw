import time
import subprocess
import pygetwindow
import json
from pathlib import Path

def launch_window(file_path: str, location: tuple[int, int], file_type: str):
    x, y = location

    if file_type == "APP":
        subprocess.Popen([file_path,])
    elif file_type == "URL":
        subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "--new-window", f"{file_path}"])

    time.sleep(0.75)

    active = pygetwindow.getActiveWindow()
    if active.isMaximized:
        active.restore()
    active.resizeTo(985,1090)

    active.moveTo(x,y)

def launch_file_explorer(file_path: str, location: tuple[int, int]):
    x, y = location

    subprocess.Popen(["explorer", file_path])

    time.sleep(0.75)
               
    active = pygetwindow.getActiveWindow()
    active.resizeTo(980,1035)

    active.moveTo(x,y)

def import_settings():
    base_directory = Path(__file__).resolve().parent
    
    return json.load(open(f"{base_directory}/filePaths.json", "r"))


if __name__ == "__main__":
    file_paths = import_settings()

    launch_window(file_paths["Make MKV"], (2880,0), "APP")
    launch_window(file_paths["Jellyfin Dashboard"], (1915,0), "URL")

    launch_file_explorer(file_paths["Jellyfin SMB"], (-10,0))
    launch_file_explorer("D:\Jellyfin Temp", (950,0))