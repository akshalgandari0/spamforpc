#install pyautogui first if you want run this file
#example = pip install pyautogui
#created by @akshalgandari

import pyautogui
import time

want=input("\nwhats a text?: ")
p=int(input('\nhow many? '))
print("\nPLEASE WAIT")

count = 5
while(count != 0) :
    time.sleep(1)
    print(count)
    count -= 1

print("\nSTART")

for i in range(0, int(p)):
    pyautogui.typewrite(want + "\n")
print("\nCOMPLETED")