import pyautogui
import time
from tkinter import Tk

#Zoom 100%, Chrome
#Tela notebook

city = {1288: 86, 1283: 86, 1429: 99, 1274: 97, 1249: 122, 1270: 98, 910: 101, 1272: 103, 1295: 104,
        1300: 105, 1331: 98, 969: 106, 1355: 107, 1363: 108, 1390: 109, 1410: 111, 1409: 110,
        1458: 115, 1067: 116, 909: 128, 1426: 113, 1443: 114, 1276: 98}

topic = [255, 279, 262, 473, 568, 564, 503, 493, 507, 382, 628, 588, 592, 554, 540]

def distribuicao(n):
    i = 1

    while i <= n:
        time.sleep(3)
        pyautogui.doubleClick(x=784, y=253)
        time.sleep(5)
        pyautogui.click(x=525, y=397)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        root = Tk()
        root.withdraw()  # Oculta a janela principal do Tkinter
        idAssunto = root.clipboard_get()
        root.destroy()  # Destroi a janela do Tkinter
        idAssunto = int(idAssunto)

        if idAssunto == 269 or idAssunto == '':
            pyautogui.alert('ENCAMINHAR O.S MANUAL.')
            break

        time.sleep(1)
        pyautogui.click(x=242, y=205)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        root = Tk()
        root.withdraw()
        idCidade = root.clipboard_get()
        root.destroy()
        idCidade = int(idCidade)

        pyautogui.click(x=660, y=157)
        time.sleep(1)
        pyautogui.click(x=673, y=213)
        time.sleep(1)
        pyautogui.click(x=533, y=218)
        pyautogui.hotkey('ctrl', 'a')

        for cidade, destino in city.items():

            if idCidade == 1426 or idCidade == 1443:
                if idAssunto == 391:
                    pyautogui.alert('ENCAMINHAR O.S MANUAL.')
                    i = 999
                    break

                for j in range(len(topic)):
                    if idAssunto == topic[j]:
                        pyautogui.write(str('98'))
                        pyautogui.click(x=669, y=340)
                        time.sleep(1)
                        pyautogui.write('REALIZAR SERVICO.')
                        time.sleep(0.5)
                        pyautogui.click(x=151, y=163)
                        time.sleep(2)
                        idCidade = 0
                        break

            if idCidade == cidade:

                pyautogui.write(str(destino))
                pyautogui.click(x=669, y=340)
                time.sleep(1)
                pyautogui.write('REALIZAR SERVICO.')
                time.sleep(0.5)
                pyautogui.click(x=151, y=163)
                time.sleep(2)
                idCidade = 0

        pyautogui.click(x=1810, y=127)
        time.sleep(9)

        i += 1

    pyautogui.alert('DISTRIBUIÇÃO CONCLUIDA!')