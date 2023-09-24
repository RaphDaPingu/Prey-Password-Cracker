import pyautogui
import pydirectinput
import win32api, win32con
import time

list_of_possible_passwords = ['{0:04}'.format(num) for num in range(0, 10000)]

# 1. Have Prey on Windowed Mode
# 2. Walk up to any keypad. Make sure to be near it and look at it or else the script will fail
# 3. Open this script while having Prey directly being the program below this script's, so that when the script will try to click in the middle of the screen it will focus on Prey
# 4. Go to sleep because of how long this will take (approx. 12-14 hours)

width, height = pyautogui.size()
pyautogui.click(width / 2, height / 2)
pydirectinput.press("esc")
pydirectinput.press("f")

for password in list_of_possible_passwords:
    for i in range(4):
        if (password[i] == "0"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 550, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -550, 0, 0)

        if (password[i] == "1"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -300, -300, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 300, 300, 0, 0)

        if (password[i] == "2"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -300, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 300, 0, 0)

        if (password[i] == "3"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 300, -300, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -300, 300, 0, 0)

        if (password[i] == "4"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -300, 0, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 300, 0, 0, 0)

        if (password[i] == "5"):
            time.sleep(0.001)
            pydirectinput.press("f")

        if (password[i] == "6"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 300, 0, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -300, 0, 0, 0)

        if (password[i] == "7"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -300, 250, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 300, -250, 0, 0)

        if (password[i] == "8"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 300, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -300, 0, 0)

        if (password[i] == "9"):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 300, 250, 0, 0)
            time.sleep(0.001)
            pydirectinput.press("f")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -300, -250, 0, 0)

    time.sleep(2.7)

    
    
