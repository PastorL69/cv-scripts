import pyautogui

pyautogui.FAILSAFE = True

duration = 0.7
switch = 2 

column = 6

startingX = 112
StartingY = 760

phaseOneCopyX1 = 5
phaseOneCopyY1 = 655

PhaseOnePasteX1 = 66
PhaseOnePasteY1 = 700

def clear_selected_pixels(clearX1, clearY1, clearX2, clearY2, phase):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')

    pyautogui.moveTo(clearX1, clearY1, duration=duration)
    pyautogui.dragTo(clearX2, clearY2, duration=duration)

    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

def select_and_copy_pixels(copyX1, copyY1, copyX2, copyY2):
    pyautogui.moveTo(copyX1, copyY1, duration=duration)

    pyautogui.keyDown('ctrl')
    pyautogui.dragTo(copyX2, copyY2, duration=duration)
    pyautogui.hotkey('c', interval=duration)

def paste_copied_pixels(pasteX1, pasteY1):
    pyautogui.keyDown('ctrl')
    pyautogui.hotkey('v', interval=duration)
    pyautogui.keyUp('ctrl')

    pyautogui.moveTo(pasteX1, pasteY1, duration=duration)
    pyautogui.leftClick()

def right_or_left(type, phase):
    for i in range(phase):
        pyautogui.hotkey(f'{type}', interval=duration)

def phaseOne():
    phase = 1
    coljumpX = 120
    coljumpY = -360

    for i in range(switch):
        select_and_copy_pixels(startingX + (column * coljumpX), 
                               StartingY + (i * coljumpY), 
                               phaseOneCopyX1 + (column * coljumpX), 
                               phaseOneCopyY1 + (i * coljumpY))
        
        clear_selected_pixels(startingX + (column * coljumpX), 
                              StartingY + (i * coljumpY), 
                              phaseOneCopyX1 + (column * coljumpX), 
                              phaseOneCopyY1 + (i * coljumpY), phase)
        
        right_or_left('right', phase)
        print(i)
        paste_copied_pixels(PhaseOnePasteX1 + (column * coljumpX), PhaseOnePasteY1 + (i * coljumpY+9))
        right_or_left('left', phase)


phaseOne()
#print(pyautogui.position())
