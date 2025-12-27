import time
import subprocess
import pygetwindow
import json
from pathlib import Path

def get_relevant_window(app_name: str):
    window = []
    timeout = 0

    while window == [] and timeout <= 5:    
        window = pygetwindow.getWindowsWithTitle(app_name)
        time.sleep(0.1)
        timeout += 0.1

    return window[0]

def launch_window(file_path: str, location: tuple[int, int], file_type: str, app_name: str = None):
    x, y = location

    if file_type == "APP":
        subprocess.Popen([file_path,])
    elif file_type == "URL":
        subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "--new-window", f"{file_path}"])
    elif file_type == "FOLDER":
        subprocess.Popen(["explorer", file_path])
        app_name = "File Explorer"

    time.sleep(1)

    active = get_relevant_window(app_name)
    
    if active.isMaximized or active.isMinimized:
        active.restore()

    if file_type == "FOLDER":
        active.resizeTo(980,1035)
    else:
        active.resizeTo(985,1090)

    active.moveTo(x,y)

def import_settings():
    base_directory = Path(__file__).resolve().parent

    return json.load(open(f"{base_directory}/filePaths.json", "r"))


if __name__ == "__main__":
    file_paths = import_settings()

    launch_window(file_paths["Make MKV"], (2880,0), "APP", "MakeMKV")
    launch_window(file_paths["Jellyfin Dashboard"], (1915,0), "URL", "Chrome")

    launch_window(file_paths["Jellyfin SMB"], (-10,0), "FOLDER")
    launch_window(file_paths["Jellyfin Temp"], (950,0), "FOLDER")