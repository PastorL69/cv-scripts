import pyautogui

print(pyautogui.position())

pyautogui.moveTo(300, 250, duration=2)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(460, 590, duration=3)  # move mouse relative to its current position