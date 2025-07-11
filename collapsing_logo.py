import pyautogui

pyautogui.FAILSAFE = True

duration = 0.8 # duration of action
switch = 2 # bottom and top
coljumpX = 120 # represents the amount of pixels to shift sideways
column = 0 # current column, maximum of 14 (15 total)
coljumpCorrection = 30 # pixels to shit downwards to successfully paste the top portion

startingX = 112
StartingY = 760

phaseOneCopyX1 = 5
phaseOneCopyY1 = 655

PhaseOnePasteX1 = 66
PhaseOnePasteY1 = 700

def select_copy_and_clear_pixels(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1, duration=duration)

    pyautogui.keyDown('ctrl')
    pyautogui.dragTo(x2, y2, duration=duration)
    pyautogui.hotkey('c', interval=duration)

    pyautogui.keyDown('shift')
    pyautogui.moveTo(x1, y1, duration=duration)
    pyautogui.dragTo(x2, y2, duration=duration)
    
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

def paste_copied_pixels(x1, y1):
    pyautogui.keyDown('ctrl')
    pyautogui.hotkey('v', interval=duration)
    pyautogui.keyUp('ctrl')

    pyautogui.moveTo(x1, y1, duration=duration)
    pyautogui.leftClick()

def right_or_left(type, phase):
    for i in range(phase):
        pyautogui.keyDown(f'{type}')
        pyautogui.keyUp(f'{type}')

def phase_one():
    phase = 1
    coljumpX = 120
    coljumpY = -360
    coljumpCorrection = 30

    for i in range(switch):
        select_copy_and_clear_pixels(startingX + (column * coljumpX), 
                               StartingY + (i * coljumpY), 
                               phaseOneCopyX1 + (column * coljumpX), 
                               phaseOneCopyY1 + (i * coljumpY))

        right_or_left('right', phase)
        paste_copied_pixels(PhaseOnePasteX1 + (column * coljumpX), PhaseOnePasteY1 + (i * (coljumpY+coljumpCorrection)))
        right_or_left('left', phase)

def phase_two():
    phase = 2

    for i in range(switch):
        coljumpY = -170
        select_copy_and_clear_pixels(111 + (column * coljumpX), 
                               624 + (i * coljumpY), 
                               7 + (column * coljumpX), 
                               595 + (i * coljumpY))

        right_or_left('right', phase)
        paste_copied_pixels(67 + (column * coljumpX), 594 + (i * (coljumpY+coljumpCorrection)))
        right_or_left('left', phase)

phase_two()
#print(pyautogui.position())
