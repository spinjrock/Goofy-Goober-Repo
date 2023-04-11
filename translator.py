import pyautogui
import keyboard
import time

with open(input("FILENAME: "), "r") as f:
    tables = f.readlines()

print (tables)

keyboard.wait("\n")
time.sleep(3)
def thing():
    for line in tables:
        line.replace("\n","")
        print(line)
        pyautogui.write(line, 0.005)
    pyautogui.write("\n")
thing()
