import pyautogui
import time
from datetime import datetime

#OBTENDO HORA DO COMPUTADOR
data_e_hora_atuais = datetime.now()
hora = data_e_hora_atuais.strftime("%H")

#VALIDANDO QUAL HORÁRIO ESTAMOS E QUAL PLAYLIST DEVERÁ SER TOCADA
if int(hora) >= 7  and int(hora) <= 12:
    #ABRINDO SPOTIFY
    pyautogui.moveTo(37,58)
    pyautogui.leftClick()
    time.sleep(15)
    #SELECIONANDO PLAYLIST
    pyautogui.moveTo(113,511)
    pyautogui.leftClick()
    time.sleep(5)
    #CLICANDO NO PLAY
    pyautogui.moveTo(210,442)
    pyautogui.leftClick()

elif int(hora)> 12 and int(hora) < 17:
    #ABRINDO SPOTIFY
    pyautogui.moveTo(37,58)
    pyautogui.leftClick()
    time.sleep(15)
    #SELECIONANDO PLAYLIST
    pyautogui.moveTo(109,438)
    pyautogui.leftClick()
    time.sleep(5)
    #CLICANDO NO PLAY
    pyautogui.moveTo(210,442)
    pyautogui.leftClick()


else:
    #ABRINDO SPOTIFY
    pyautogui.moveTo(37,58)
    pyautogui.leftClick()
    time.sleep(15)
    #ESCOLHENDO PLAYLIST
    pyautogui.moveTo(108,381)
    pyautogui.leftClick()
    time.sleep(5)
    #CLICANDO NO PLAY
    pyautogui.moveTo(210,442)
    pyautogui.leftClick()