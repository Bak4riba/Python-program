import pyautogui
import time
#c = 0
#while c < 10:
#    time.sleep(3)
#    print(pyautogui.position())
#    c = c + 1
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%H")
if int(data_e_hora_em_texto) > 7  and int(data_e_hora_em_texto) < 12:
    print('manha')
elif int(data_e_hora_em_texto)> 12 and int(data_e_hora_em_texto) < 17:
    print("tarde")
else:
    print('noite')
    