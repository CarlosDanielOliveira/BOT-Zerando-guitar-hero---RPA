from time import sleep 
import keyboard
import pyautogui as pa



while keyboard.is_pressed(1) == False:
    if pa.pixelMatchesColor(749,812,(0,152,0)) :
        pa.press('a')
        

    if pa.pixelMatchesColor(848,813,(255,0,0)) : 
        pa.press('s')
        

    if pa.pixelMatchesColor(945,815,(244,244,2)) :
        pa.press('j')
         

    if pa.pixelMatchesColor(1043,813,(0,152,255)): 
        pa.press('k')
        


