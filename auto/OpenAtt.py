import pyautogui
import time
from tkinter import Tk

def fecharOsAudit():
    pyautogui.click(x=668, y=278)
    time.sleep(0.5)
    pyautogui.click(x=671, y=435)
    time.sleep(1)
    pyautogui.click(x=672, y=376)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.press('delete')

    pyautogui.write('>>TIPO DE ALTERAÇÃO: TROCA DE EQUIPAMENTO \n'
                    'REALIZA SERVIÇO TÉCNICO: (   ) SIM | ( x  ) NÃO\n'
                    '.\n'
                    '>> EXISTE EQUIPAMENTOS EM COMODATO? (x ) SIM | (  ) NÃO\n'
                    '>> HAVERÁ TROCA DE EQUIPAMENTO EM COMODATO?  (x ) SIM | (  ) NÃO\n'
                    '- MODELOS: REALIZAR A SUBSTITUIÇÃO DE ONU E ROTEADOR PARA ONT HUAWEI DEVIDO A TROCA DE ROTAS (EPON PARA GPON).')
    time.sleep(0.5)
    pyautogui.click(x=531, y=552)
    pyautogui.write(str('7'))
    time.sleep(0.5)
    pyautogui.click(x=537, y=799)
    pyautogui.write(str('657'))
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.click(x=158, y=171)
    time.sleep(1)

def fecharOsNormal():
    pyautogui.click(x=668, y=278)
    time.sleep(0.5)
    pyautogui.click(x=671, y=435)
    time.sleep(1)
    pyautogui.click(x=672, y=376)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.press('delete')
    time.sleep(0.5)
    pyautogui.write('>>TIPO DE ALTERAÇÃO: TROCA DE EQUIPAMENTO \n'
                    'REALIZA SERVIÇO TÉCNICO: (   ) SIM | ( x  ) NÃO\n'
                    '.\n'
                    '>> EXISTE EQUIPAMENTOS EM COMODATO? (x ) SIM | (  ) NÃO\n'
                    '>> HAVERÁ TROCA DE EQUIPAMENTO EM COMODATO?  (x ) SIM | (  ) NÃO\n'
                    '- MODELOS: REALIZAR A SUBSTITUIÇÃO DE ONU E ROTEADOR PARA ONT HUAWEI DEVIDO A TROCA DE ROTAS (EPON PARA GPON).')
    time.sleep(0.5)
    pyautogui.click(x=158, y=171)
    time.sleep(1)

def atualizarLista():
    pyautogui.click(x=759, y=275)


time.sleep(0.5)
pyautogui.click(x=839, y=501)
time.sleep(3)
pyautogui.click(x=839, y=208)
time.sleep(1)
pyautogui.click(x=155, y=272)
time.sleep(2)
pyautogui.click(x=521, y=511)
pyautogui.write(str('198'))
pyautogui.scroll(-500)
time.sleep(1)
pyautogui.click(x=628, y=690)
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.press('delete')

pyautogui.write('>>TIPO DE ALTERAÇÃO: TROCA DE EQUIPAMENTO \n'
                'REALIZA SERVIÇO TÉCNICO: (   ) SIM | ( x  ) NÃO\n'
                '.\n'
                '>> EXISTE EQUIPAMENTOS EM COMODATO? (x ) SIM | (  ) NÃO\n'
                '>> HAVERÁ TROCA DE EQUIPAMENTO EM COMODATO?  (x ) SIM | (  ) NÃO\n'
                '- MODELOS: REALIZAR A SUBSTITUIÇÃO DE ONU E ROTEADOR PARA ONT HUAWEI DEVIDO A TROCA DE ROTAS (EPON PARA GPON).')
time.sleep(0.5)
pyautogui.click(x=232, y=167)
time.sleep(1)
pyautogui.click(x=815, y=214)
time.sleep(1)

####
fecharOsNormal()
####
atualizarLista()
####
fecharOsNormal()
####
atualizarLista()
####
fecharOsAudit()
####
time.sleep(0.5)
pyautogui.click(x=1820, y=136)
time.sleep(0.2)
pyautogui.click(x=1818, y=131)
time.sleep(0.2)
pyautogui.click(x=1813, y=128)