import pyautogui
import time
from tkinter import Tk

city = {1288: 86, 1429: 99, 1274: 97, 1249: 122, 1270: 98, 910: 101, 1272: 103, 1295: 104,
        1300: 105, 1331: 98, 969: 106, 1355: 107, 1363: 108, 1390: 109, 1410: 111, 1409: 110,
        1458: 115, 1067: 116, 909: 128, 1426: 113, 1443: 114}

topic = [255, 279, 262, 473, 568, 564, 503, 493, 507, 382, 628, 588, 592, 554, 540]

def distribuicao(n):
    i = 1

    while i <= n:
        pyautogui.doubleClick(x=250, y=219)
        time.sleep(5)
        pyautogui.click(x=518, y=462)
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
        pyautogui.click(x=254, y=253)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        root = Tk()
        root.withdraw()
        idCidade = root.clipboard_get()
        root.destroy()
        idCidade = int(idCidade)

        pyautogui.click(x=722, y=201)
        time.sleep(1)
        pyautogui.click(x=729, y=264)
        time.sleep(1)
        pyautogui.click(x=541, y=271)
        pyautogui.hotkey('ctrl', 'a')

        for cidade, destino in city.items():

            if idCidade == 1426:
                if idAssunto == 391:
                    pyautogui.alert('ENCAMINHAR O.S MANUAL.')
                    break

                for j in range(len(topic)):
                    if idAssunto == topic[j]:
                        pyautogui.write(str('98'))
                        pyautogui.click(x=649, y=424)
                        time.sleep(0.5)
                        pyautogui.write('REALIZAR SERVICO.')
                        time.sleep(0.5)
                        pyautogui.click(x=158, y=206)
                        time.sleep(2)
                        idCidade = 0
                        break

            if idCidade == 1443:
                if idAssunto == 391:
                    pyautogui.alert('ENCAMINHAR O.S MANUAL.')
                    break

                for l in range(len(topic)):
                    if idAssunto == topic[l]:
                        pyautogui.write(str('98'))
                        pyautogui.click(x=649, y=424)
                        time.sleep(0.5)
                        pyautogui.write('REALIZAR SERVICO.')
                        time.sleep(0.5)
                        pyautogui.click(x=158, y=206)
                        time.sleep(2)
                        idCidade = 0
                        break

            if idCidade == cidade:

                pyautogui.write(str(destino))
                pyautogui.click(x=649, y=424)
                time.sleep(0.5)
                pyautogui.write('REALIZAR SERVICO.')
                time.sleep(0.5)
                pyautogui.click(x=158, y=206)
                time.sleep(2)
                idCidade = 0

        pyautogui.click(x=1812, y=169)
        time.sleep(7)

        i += 1

    pyautogui.alert('DISTRIBUIÇÃO CONCLUIDA!')