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
        time.sleep(2)
        pyautogui.doubleClick(x=882, y=252)
        time.sleep(2)
        pyautogui.click(x=522, y=394)
        time.sleep(0.5)

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
        pyautogui.click(x=233, y=204)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        root = Tk()
        root.withdraw()
        idCidade = root.clipboard_get()
        root.destroy()
        idCidade = int(idCidade)

        pyautogui.click(x=488, y=159)
        time.sleep(1)
        pyautogui.click(x=491, y=216)
        time.sleep(1)
        pyautogui.click(x=501, y=219)
        time.sleep(0.5)
        pyautogui.click(x=530, y=254)
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
                        pyautogui.click(x=550, y=373)
                        time.sleep(0.5)
                        pyautogui.write('REALIZAR SERVICO.')
                        time.sleep(0.5)
                        pyautogui.click(x=175, y=160)
                        time.sleep(1)
                        idCidade = 0
                        break

            if idCidade == cidade:

                pyautogui.write(str(destino))
                pyautogui.click(x=550, y=373)
                time.sleep(0.5)
                pyautogui.write('REALIZAR SERVICO.')
                time.sleep(0.5)
                pyautogui.click(x=175, y=160)
                time.sleep(1)
                idCidade = 0

        pyautogui.click(x=1813, y=129)
        time.sleep(1)

        i += 1

    pyautogui.alert('DISTRIBUIÇÃO CONCLUIDA!')