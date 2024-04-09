import pyautogui
import time
from datetime import datetime

#OBTENDO HORA DO COMPUTADOR
data_e_hora_atuais = datetime.now()
hora = data_e_hora_atuais.strftime("%H")
dia = data_e_hora_atuais.strftime("%D")

#VALIDANDO QUAL HORÁRIO ESTAMOS E QUAL PLAYLIST DEVERÁ SER TOCADA
if int(hora) >= 7  and int(hora) <= 12:
    ##ABRINDO SPOTIFY
    #pyautogui.moveTo(37,58)
    #pyautogui.leftClick()
    #time.sleep(15)
    ##SELECIONANDO PLAYLIST
    #pyautogui.moveTo(113,511)
    #pyautogui.leftClick()
    #time.sleep(5)
    ##CLICANDO NO PLAY
    #pyautogui.moveTo(210,442)
    #pyautogui.leftClick()
    with open("log.txt", "a") as file1:
        file1.write("\n OK Manha - " + data_e_hora_atuais.strftime("%H:%M") + " " + dia )
    

elif int(hora)> 12 and int(hora) < 17:
    ##ABRINDO SPOTIFY
    #pyautogui.moveTo(37,58)
    #pyautogui.leftClick()
    #time.sleep(15)
    ##SELECIONANDO PLAYLIST
    #pyautogui.moveTo(109,438)
    #pyautogui.leftClick()
    #time.sleep(5)
    ##CLICANDO NO PLAY
    #pyautogui.moveTo(210,442)
    #pyautogui.leftClick()
    with open("log.txt", "a") as file1:
        file1.write("\n OK Tarde - " + data_e_hora_atuais.strftime("%H:%M") + " " + dia  )
    


else:
    ##ABRINDO SPOTIFY
    #pyautogui.moveTo(37,58)
    #pyautogui.leftClick()
    #time.sleep(15)
    ##ESCOLHENDO PLAYLIST
    #pyautogui.moveTo(108,381)
    #pyautogui.leftClick()
    #time.sleep(5)
    ##CLICANDO NO PLAY
    #pyautogui.moveTo(210,442)
    #pyautogui.leftClick()
    with open("log.txt", "a") as file1:
        file1.write("\n OK Noite - " + data_e_hora_atuais.strftime("%H:%M") + " " + dia )
    
