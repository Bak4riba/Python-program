import pyautogui
import time
from datetime import datetime

#OBTENDO HORA DO COMPUTADOR
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%H")

##
if int(data_e_hora_em_texto) > 7  and int(data_e_hora_em_texto) < 12:
    print('manha')
elif int(data_e_hora_em_texto)> 12 and int(data_e_hora_em_texto) < 17:
    print(data_e_hora_em_texto)

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
else:
    print('noite')




#pyautogui.write(link)
#time.sleep(1)
#pyautogui.press('enter')

