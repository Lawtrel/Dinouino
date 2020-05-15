import subprocess   
import time
import pyautogui
import serial
subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe',  
    '-new-tab', 'https://chromedino.com/'])  
time.sleep(6)

ser = serial.Serial('COM4')		
ser.baudrate = '9600'			

while True:						
  dino=ser.readline()
  if dino:
   pule = int(dino.decode('utf-8'))
   if pule== 1:
   	print("Pule!! ")		
   	pyautogui.press('up') 