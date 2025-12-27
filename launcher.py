import pyautogui
import time
import subprocess
import pygetwindow
import keyboard

def launch_window(file_path: str, location: tuple, file_type: str):
    x = location[0]
    y = location[1]

    if file_type == "APP":
        subprocess.Popen([file_path,])
    elif file_type == "URL":
        subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "--new-window", f"{file_path}"])

    time.sleep(0.75)

    active = pygetwindow.getActiveWindow()
    if active.isMaximized:
        active.restore()
    active.resizeTo(985,1090)

    active = pyautogui.getActiveWindow()
    active.moveTo(x,y)

def get_pos():
    print(pyautogui.position())


launch_window("D:/Apps/MakeMKV/makemkv.exe", (2880,0), "APP")
launch_window("http://192.168.1.155:30013/web/#/home", (1915,0), "URL")

pyautogui.moveTo(2846, 111)
pyautogui.click()

time.sleep(0.25)

pyautogui.moveTo(2282, 760)
pyautogui.click()

keyboard.add_hotkey("b", get_pos)
keyboard.wait()