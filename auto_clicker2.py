import pyautogui
import time
import random
from pynput import mouse
import keyboard

clicking = False

def on_click(x,y,button, pressed):
    global clicking
    if pressed:
        if button == mouse.Button.x2:  
            clicking = True
        elif button == mouse.Button.x1:  
            clicking = False
              
listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    if clicking:
        pyautogui.click()
        random_number = random.uniform(0.001, 0.034)  
        time.sleep(random_number)
    
    time.sleep(0.01)  
    if keyboard.is_pressed('`'):
        break

listener.stop()