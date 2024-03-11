import pyautogui
import time
from datetime import datetime

#OBTENDO HORA DO COMPUTADOR
data_e_hora_atuais = datetime.now()
hora = data_e_hora_atuais.strftime("%H")

##VALIDANDO QUAL HORÁRIO ESTAMOS E QUAL PLAYLIST DEVERÁ SER TOCADA
if int(hora) > 7  and int(hora) < 12:
    pyautogui.press("win")
    pyautogui.write('spotify')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(98,150,0.5)
    pyautogui.click(button='left')
    time.sleep(2)
    pyautogui.write('Dom Bosco - Manhã')
    pyautogui.moveTo(622,416,0.5)
    time.sleep(3)
    pyautogui.click(button='left')
elif int(hora)> 12 and int(hora) < 17:

    pyautogui.press("win")
    pyautogui.write('spotify')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(98,150,0.5)
    pyautogui.click(button='left')
    time.sleep(2)
    pyautogui.write('Tarde - Dom Bosco')
    pyautogui.moveTo(622,416,0.5)
    time.sleep(3)
    pyautogui.click(button='left')
else:
    pyautogui.press("win")
    pyautogui.write('spotify')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(98,150,0.5)
    pyautogui.click(button='left')
    time.sleep(2)
    pyautogui.write('UNIFATEB')
    pyautogui.moveTo(622,416,0.5)
    time.sleep(3)
    pyautogui.click(button='left')

