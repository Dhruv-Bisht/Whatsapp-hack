import pyautogui
import time

time.sleep(4)
count = 0

msg = input("Enter the message:")
No_of_time = int(input("Enter the no of times message to be sent:"))
while count <= No_of_time:
    pyautogui.typewrite(msg)  
    pyautogui.press('enter')
    count += 1





